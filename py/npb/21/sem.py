#! /usr/bin/env python
# -*- coding:UTF-8 -*-
# 使用信号量机制，注意semaphore的使用
# sem可以管理某一类资源的一组实例
# 其实使用queue队列模块是最佳的

import threading
import time
import random

def numbergen(sem, queue, qlock):
    while True:
        time.sleep(2)
        if random.randint(0,1):
            value = random.randint(1,100)
            qlock.acquire()       # 第二道岗，可以独占队列
            try:
                queue.append(value)
            finally:
                qlock.release()
            print "Placed %d on the queue." % value
            sem.release() #第一道岗，表明对消费者来说数据已经可以使用了，数字不一定马上处理

def numbercal(sem, queue, qlock):
    while True:
        sem.acquire()
        qlock.acquire()
        try:
            value = queue.pop(0)
        finally:
            qlock.release()
        print "%s: Got %d from the queue."%\
                (threading.currentThread().getName(),value)
        newvalue = value * 2
        time.sleep(3)
        
# 主线程,共享变量，参数传递
childthreads = []
sem = threading.Semaphore(0)
queue = []
qlock = threading.Lock()

# 创建生产线程
t = threading.Thread(target = numbergen, args = [sem, queue, qlock])
t.setDaemon(True)
t.start()
childthreads.append(t)

# 创建消费线程
for i in range(1,3):
    t = threading.Thread(target = numbercal, args= [sem,queue, qlock])
    t.setDaemon(True)
    t.start()
    childthreads.append(t)

while True: #forever
    time.sleep(300)
