#!/usr/bin/env python
# -*- coding:UTF-8

""" 
	放置结束标志的模型

	生产者在队列中放入标志，通知使用者,生产者不再生产任何数据
	用途是可以更主动的控制消费者的队列项目消费

	此外，消费者进程不必再设置为daemon进程
	消费者进程多少个，放置的结束标志就需要有多少

""" 

import multiprocessing
import time

def consumer(input_q):
    while True:
        item = input_q.get()
        if item is None:
             break
        print item              #实际工作

    # 这里可以有好多其他的工作...
    print "%s will terminated after 6 seconds" % multiprocessing.current_process().name
    time.sleep(6)
    print "%s terminated " % multiprocessing.current_process().name

def producer(seq,output_q):
    for item in seq:
        output_q.put(item)

if __name__ == '__main__':
    q = multiprocessing.Queue()

    # 可以有好多使用者进程 
    processes = []          #不错
    for num in range(5):
        p = multiprocessing.Process(target=consumer,name="Process %d" % num, args=(q,))
        processes.append(p)
        p.start()

    seq = xrange(100) 
    producer(seq,q)

    for sig in xrange(5):   #放置None标志,发出完成标志 
        q.put(None)    
    
    for p in processes:
        p.join()   #等待使用者进程结束 
    print "Main Process Terminated!"
