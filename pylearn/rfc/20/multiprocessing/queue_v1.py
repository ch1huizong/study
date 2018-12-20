#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# 两个使用者和生产者进程
import multiprocessing
import time

def consumer(input_q):
    while True:
        item = input_q.get()
        print item              #可以换成实际的处理工作
        input_q.task_done()
        time.sleep(15)

def producer(seq,output_q):
    for item in seq:
        output_q.put(item)

if __name__ == '__main__':
    q = multiprocessing.JoinableQueue()  #共享队列

    cons_p1 = multiprocessing.Process(name = "P1",target=consumer,args=(q,))
    cons_p1.daemon = True  # 主进程结束，它也结束,否则一直运行下去
    cons_p1.start()

    cons_p2 = multiprocessing.Process(name = "P2",target=consumer,args=(q,))
    cons_p2.daemon = True
    cons_p2.start()

    seq = [1,2,3,4,5]
    producer(seq,q)
    q.join()    # 等待队列项目消耗完毕,如何获得通知？q.taskdone
                # 关注点是队列，不是等待子进程结束
    print "Main Terminated."
