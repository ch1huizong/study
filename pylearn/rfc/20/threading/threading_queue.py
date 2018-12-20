#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# valuable
""" 类似协程的基于队列的生产者-消费者模型

    队列在一个子线程内还是在主控线程中是不重要的，
    关键是在这个队列两端可以有接口,
    通过这个接口(父子进程中可能不一样)，
    子线程之间传送数据。

"""
import threading
from Queue import Queue

class WorkerThread(threading.Thread):
    def __init__(self,*args,**kwargs):
        threading.Thread.__init__(self,*args,**kwargs)
        self.input_queue = Queue()

    def send(self,item):  # 接口 
        self.input_queue.put(item)

    def close(self):   # 接口 
        self.input_queue.put(None)
        self.input_queue.join()  # 主控等待queue结束
    
    def run(self):
        while True:    # 注意
            item = self.input_queue.get()
            if item is None:    #标志
                break
            print item
            self.input_queue.task_done()
        self.input_queue.task_done() # !很重要
        return

w = WorkerThread()
w.start()
w.send("hello")
w.send("world")
w.close()
