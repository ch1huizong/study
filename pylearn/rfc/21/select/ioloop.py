#! /usr/bin/env python
# -*- coding:UTF-8 -*-
# 基于协程（任务）的io调度
# 关键是嵌套协程的理解

import select
import types
import collections

class Task(object):

    def __init__(self, target):
        self.target = target
        self.sendval = None     # 嵌套协程直接相互传递的结果还有意义
        self.stack = []

    def run(self):
        try:
            result = self.target.send(self.sendval)

            if isinstance(result, SystemCall): # 需要调度主控执行一些操作
                return result

            if isinstance(result, types.GeneratorType):
                self.stack.append(self.target)  # 任务的当前协程保存
                self.sendval = None
                self.target = result # 控制权转移到返回的协程

            else:
                if not self.stack: return   # 当前执行的协程是唯一的协程?

                self.sendval = result   # defer一次值传递？
                self.target = self.stack.pop() # 上层协程恢复,等到内曾发给它的一个值

        except StopIteration: # 已经终止的协程
            # 传播异常，通知主控这个任务已经完成，主控会捕捉异常并进行处理
            if not self.stack: raise  

            self.sendval = None  # 控制权转移
            self.target = self.stack.pop() # 下层协程消耗殆尽, 上层协程跳出

class SystemCall(object):
    def handle(self, sched,task):
        pass

class ReadWait(SystemCall): 

    def __init__(self, f):
        self.f = f 

    def handle(self, sched, task):
        fileno = self.f.fileno()
        sched.readwait(task, fileno) 

class WriteWait(SystemCall):

    def __init__(self, f):
        self.f = f

    def handle(self, sched, task):
        fileno = self.f.fileno()
        sched.writewait(task, fileno)

class NewTask(SystemCall):

    def __init__(self, target):
        self.target = target

    def handle(self, sched, task):
        sched.new(self.target)
        sched.schedule(task) # 本任务再次调进
        

class Scheduler(object):

    def __init__(self):
        self.task_queue = collections.deque() # "正运行"队列
        self.read_waiting = {}  
        self.write_waiting = {}  
        self.numtasks = 0
    
    def schedule(self, task):
        self.task_queue.append(task)

    def new(self, target):
        newtask = Task(target)
        self.schedule(newtask)
        self.numtasks += 1
    
    # 让任务等待文件描述符fd上的数据
    def readwait(self,task,fd):  
        self.read_waiting[fd] = task

    def writewait(self,task, fd):
        self.write_waiting[fd] = task


    def mainloop(self, count=-1, timeout=None): # count控制运行次数
        while self.numtasks: # loop1,未完成总任务

            # 查询一下IO
            if self.read_waiting or self.write_waiting:
                # 第二次运行到这里，task_queue必然没有任务？
                # bug?
                wait = 0 if self.task_queue else timeout 
                r,w,e = select.select(self.read_waiting,self.write_waiting,[], wait)

                for fileno in r:
                    # 把相应fd的读task调出，并调入中心调度器的任务队列
                    self.schedule(self.read_waiting.pop(fileno)) 
                for fileno in w:
                    self.schedule(self.write_waiting.pop(fileno)) 

            # loop2, 运行队列上所有的任务, 
            # 会消耗完运行队列,numtasks可能就还剩阻塞态的了
            while self.task_queue:
                task = self.task_queue.popleft() # "调出"任务队列
                try:
                    result = task.run() 
                    if isinstance(result, SystemCall):
                        result.handle(self,task) # 系统调用去处理, 调入等待区
                    else:
                        self.schedule(task)  # 其他的结果task再"加入"进去队列
                except StopIteration:
                    self.numtasks -= 1  # 一个任务结束了
            else:
                if count > 0 : count -= 1  # 是控制运行次数，但场景？
                if count == 0 : 
                    return


if __name__ == '__main__':
    from socket import socket, AF_INET, SOCK_STREAM
    import time
    def timeserver(address):
        s = socket(AF_INET,SOCK_STREAM)
        s.bind(address)
        s.listen(5)
        while True:
            # 停, 每个任务会自己产生阻塞点, 调入"运行队列"后，后面的就不会阻塞
            yield ReadWait(s)  
            conn, addr = s.accept()
            print "Connection from %s" % str(addr)
            yield WriteWait(conn)
            resp = time.ctime() + "\r\n"
            conn.send(resp.encode('ascii')) # 可以发送了
            conn.close()

    sched = Scheduler()
    sched.new(timeserver(('',10000)))
    sched.new(timeserver(('',11000)))
    sched.mainloop()
