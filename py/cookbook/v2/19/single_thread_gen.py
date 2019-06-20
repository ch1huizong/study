#! /usr/bin/env python
# -*- coding:UTF-8 -*-

import sys
import threading
import Queue


class Single_Thread_Gen(threading.Thread):
    """既包含生产能力又包含消费能力,
       最后返回迭代器
    """
    
    def __init__(self, iterable, queuesize=0):
        threading.Thread.__init__(self)
        self.iterable = iterable
        self.queuesize = queuesize

    def stop(self):
        self.stopRequested = True

    def run(self):
        put = self.queue.put
        try:
            itnext = iter(self.iterable).next
            while True:
                put((False, itnext()))  # 生成 
                if self.stopRequested:
                    raise StopIteration
        except:
            put((True, sys.exc_info()))

    def execute(self):  
        self.queue = Queue.Queue(self.queuesize)
        get = self.queue.get
        self.stopRequested = False
        self.run()
        while True:
            mark, item = get()
            if mark:
                break
            yield item    # 获得
        exc_type, exc_value, traceback = item
        if not isinstance(exc_type, StopIteration):
            raise exc_type, exc_value, traceback
    def __iter__(self):
        return iter(self.execute())
 
if __name__ == '__main__':
    pass




        
            

            



