#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#
# ------------------------------------------------------------
#
# pyos7.py  -  The Python Operating System
#
#
# Step 6 : I/O Waiting Support added
#
# ***里面跑着一个监控进程，根据io状态不停的移进/移出client/master部分***
#
# ------------------------------------------------------------

# ------------------------------------------------------------
#                       === Tasks ===
# ------------------------------------------------------------
class Task(object):
    taskid = 0
    def __init__(self,target):
        Task.taskid += 1
        self.tid     = Task.taskid   # Task ID
        self.target  = target        # Target coroutine
        self.sendval = None          # Value to send

    # Run a task until it hits the next yield statement
    def run(self):
        return self.target.send(self.sendval)


# ------------------------------------------------------------
#                      === Scheduler ===
# ------------------------------------------------------------
from Queue import Queue
import select

class Scheduler(object):
    def __init__(self):
        self.ready   = Queue()   
        self.taskmap = {}        

        # Tasks waiting for other tasks to exit
        self.exit_waiting = {}

        # I/O waiting
        self.read_waiting = {}
        self.write_waiting = {}
        
    def new(self,target):
        newtask = Task(target)
        self.taskmap[newtask.tid] = newtask
        self.schedule(newtask)
        return newtask.tid

    def exit(self,task):
        print "Task %d terminated" % task.tid
        del self.taskmap[task.tid]
        # Notify other tasks waiting for exit
        for task in self.exit_waiting.pop(task.tid,[]):
            self.schedule(task)

    def waitforexit(self,task,waittid):
        if waittid in self.taskmap:
            self.exit_waiting.setdefault(waittid,[]).append(task)
            return True
        else:
            return False

    # I/O waiting
    def waitforread(self,task,fd):
        self.read_waiting[fd] = task

    def waitforwrite(self,task,fd):
        self.write_waiting[fd] = task

    def iopoll(self,timeout):
        if self.read_waiting or self.write_waiting:
           r,w,e = select.select(self.read_waiting,
                                 self.write_waiting,[],timeout)
           for fd in r: self.schedule(self.read_waiting.pop(fd))
           for fd in w: self.schedule(self.write_waiting.pop(fd))

    def iotask(self): # 自己包装成一个任务，在调度器中运行
        while True:
            if self.ready.empty():  # 任务队列否还有其他的?
                self.iopoll(None)  # 永不返回
            else:
                self.iopoll(0)  # 查询一下,立马返回
            yield

    def schedule(self,task):
        self.ready.put(task)

    def mainloop(self):  # 主处理框架,入口和出口
         self.new(self.iotask())
         while self.taskmap:
             task = self.ready.get()
             try:
                 result = task.run()
                 if isinstance(result,SystemCall):
                     result.task  = task 
                     result.sched = self
                     result.handle()
                     continue   # 出口1
             except StopIteration:
                 self.exit(task)
                 continue   # 出口2
             self.schedule(task) # 默认出口3,iotask默认走这

# ------------------------------------------------------------
#                   === System Calls ===
# ------------------------------------------------------------

class SystemCall(object):
    def handle(self):
        pass

# Return a task's ID number
class GetTid(SystemCall):
    def handle(self):
        self.task.sendval = self.task.tid
        self.sched.schedule(self.task)

# Create a new task
class NewTask(SystemCall):
    def __init__(self,target):
        self.target = target
    def handle(self):
        tid = self.sched.new(self.target)
        self.task.sendval = tid
        self.sched.schedule(self.task)

# Kill a task
class KillTask(SystemCall):
    def __init__(self,tid):
        self.tid = tid
    def handle(self):
        task = self.sched.taskmap.get(self.tid,None)
        if task:
            task.target.close() 
            self.task.sendval = True
        else:
            self.task.sendval = False
        self.sched.schedule(self.task)

# Wait for a task to exit
class WaitTask(SystemCall):
    def __init__(self,tid):
        self.tid = tid
    def handle(self):
        result = self.sched.waitforexit(self.task,self.tid)
        self.task.sendval = result
        # If waiting for a non-existent task,
        # return immediately without waiting
        if not result:
            self.sched.schedule(self.task)

# Wait for reading
class ReadWait(SystemCall):
    def __init__(self,f):
        self.f = f
    def handle(self):
        fd = self.f.fileno()
        self.sched.waitforread(self.task,fd)
        # 并没有再把当前任务add进来

# Wait for writing
class WriteWait(SystemCall):
    def __init__(self,f):
        self.f = f
    def handle(self):
        fd = self.f.fileno()
        self.sched.waitforwrite(self.task,fd)

# ------------------------------------------------------------
#                      === Example ===
# ------------------------------------------------------------

# Run the script echogood.py to see this work

