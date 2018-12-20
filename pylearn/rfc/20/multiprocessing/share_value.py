#!/usr/bin/env python
# -*- coding:UTF-8
# 共享值和数组,使用了锁来同步

import multiprocessing

class FloatChannel(object):
    def __init__(self,maxsize):
        self.buffer = multiprocessing.RawArray('d',maxsize)
        self.buffer_len = multiprocessing.Value('i')
        self.empty = multiprocessing.Semaphore(1)  # 两把锁？这是什么思路？
        self.full = multiprocessing.Semaphore(0)
    
    def send(self,values):              
        self.empty.acquire()           
        num = len(values)
        self.buffer_len = num
        self.buffer[:num] = values 
        self.full.release() 

    def recv(self): 
        self.full.acquire()             # Why?
        values = self.buffer[:self.buffer_len.value]
        self.empty.release()
        return values


def consume_test(count,ch):
    for i in xrange(count):
        values = ch.recv()

def produce_test(count,values,ch):
    for i in xrange(count):
        ch.send(values)

if __name__ == '__main__':
    ch = FloatChannel(100000)
    p = multiprocessing.Process(target=consume_test,\
                    args=(1000,ch))
    p.start()

    values = [ float(x) for x in xrange(100000)]
    produce_test(1000,values,ch)
    print'Done'
    p.join()


