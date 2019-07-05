#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#
# ------------------------------------------------------------
# pyos5.py  -  The Python Operating System
#
# Step 5: Added system calls for simple task management
# ------------------------------------------------------------

# ------------------------------------------------------------
#
# 三类对象： 
#   主循环;
#   任务对象(指向协程);
#   系统调用对象;
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
    def run(self): # 任务外部接口
        return self.target.send(self.sendval)


# ------------------------------------------------------------
#                      === Scheduler ===
# ------------------------------------------------------------
from Queue import Queue

class Scheduler(object):
    def __init__(self):
        self.ready   = Queue()  # 运行队列
        self.taskmap = {}   # 任务字典 

    def new(self,target):
        newtask = Task(target)
        self.taskmap[newtask.tid] = newtask
        self.schedule(newtask)
        return newtask.tid

    def exit(self,task):
        print "Task %d terminated" % task.tid
        del self.taskmap[task.tid]

    def schedule(self,task):
        self.ready.put(task)

    def mainloop(self):
         while self.taskmap:
            task = self.ready.get() 
            try:
                result = task.run()
                if isinstance(result, SystemCall):
                    result.task  = task   # 为系统服务保存一个环境 
                    result.sched = self
                    result.handle()  # 运行系统调用服务
                    continue
            except StopIteration:
                self.exit(task)
                continue
            self.schedule(task)  # 重新加入调度


# ------------------------------------------------------------
#                   === System Calls ===
# ------------------------------------------------------------

class SystemCall(object):
    def handle(self):
        pass

# Return a task's ID number
class GetTid(SystemCall):
    def handle(self):
        self.task.sendval = self.task.tid   # 当前任务的下一个接收值
        self.sched.schedule(self.task)

# Create a new task
class NewTask(SystemCall):
    def __init__(self,target):
        self.target = target
    def handle(self):
        tid = self.sched.new(self.target)   # 创建进程
        self.task.sendval = tid  # 发送子进程id给当前进程 
        self.sched.schedule(self.task)

# Kill a task
class KillTask(SystemCall):
    def __init__(self,tid):
        self.tid = tid
    def handle(self):
        task = self.sched.taskmap.get(self.tid,None) # 子进程可能已经结束了，所以为None 
        if task:
            task.target.close() 
            self.task.sendval = True  # 下一次发送给当前任务的值
        else:
            self.task.sendval = False  
        self.sched.schedule(self.task)


# ------------------------------------------------------------
#                      === Example ===
# ------------------------------------------------------------

if __name__ == '__main__':

    def foo():  # 业务协程
        mytid = yield GetTid()
        while True:
            print "I'm foo", mytid
            yield

    # Launch new task ,child是MainTask的sendval值,也是foo的tid
    def main(): # 父进程 
        child = yield NewTask(foo()) 
        for i in xrange(5):
            yield
        yield KillTask(child)   # 杀死子进程
        print "main done"

    # 总共有两个Task,分别是MainTask和FooTask,交替运行，MainTask会生成FooTask,
    # 并且也会销毁FooTask，有点像init父进程生成并销毁子进程
    sched = Scheduler()
    sched.new(main())
    sched.mainloop()
