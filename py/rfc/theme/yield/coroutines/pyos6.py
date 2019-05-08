#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#
# ------------------------------------------------------------
# pyos6.py  -  The Python Operating System
#
# Added support for task waiting
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

class Scheduler(object):   
    def __init__(self):
        self.ready   = Queue()  # 正运行的任务队列 
        self.taskmap = {} # 活动的任务,包括等待的和运行队列中

        # Tasks waiting for other tasks to exit
        self.exit_waiting = {} # {'被等待任务Id' : [等待者1, 等待者2...]}

    def new(self,target):
        newtask = Task(target)
        self.taskmap[newtask.tid] = newtask
        self.schedule(newtask)
        return newtask.tid

    def exit(self,task):
        print "Task %d terminated" % task.tid
        del self.taskmap[task.tid]
        # Notify other tasks waiting for exit
        for task in self.exit_waiting.pop(task.tid,[]):     # 通知所有的主动等待者,重新加入调度,进入正运行队列
            self.schedule(task)

    def waitforexit(self,task,waittid):
        if waittid in self.taskmap:  # 被等待者还没提前结束
            self.exit_waiting.setdefault(waittid,[]).append(task)   
            return True
        else:
            return False

    def schedule(self,task):
        self.ready.put(task)

    def mainloop(self):
         while self.taskmap:
            task = self.ready.get()
            try:
                result = task.run()
                if isinstance(result,SystemCall):
                    result.task  = task   # 保存一些系统调用需要用到的信息
                    result.sched = self
                    result.handle()
                    continue
            except StopIteration:
                self.exit(task)
                continue
            self.schedule(task)

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
        self.task.sendval = tid    # main task child value
        self.sched.schedule(self.task) # 当前任务重新进入调度

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
        #
        # ADD MAIN TASK  注意这里,没有再把MainTask加进taskmap
        #
        # If waiting for a non-existent task,
        # return immediately without waiting
        if not result: # 如果被等待者已经提前运行结束了
            self.sched.schedule(self.task)

# ------------------------------------------------------------
#                      === Example ===
#                   以任务为单元进行跟踪
# 流程：
#   通过在ChildTask运行期间使Maintask退出taskmap获得等待，
#   最后再把在ChildTask结束时把MainTask加进来，完成主Task退出
# ------------------------------------------------------------
if __name__ == '__main__':
    def foo():    
        yield
        for i in xrange(5):
            print "I'm foo"
            yield

    def main():   
        child = yield NewTask(foo())
        print "Waiting for child", child
        yield WaitTask(child)  # 通过调用系统服务，引用另一个task
        print "Child done"

    sched = Scheduler()
    sched.new(main())
    sched.mainloop()  
