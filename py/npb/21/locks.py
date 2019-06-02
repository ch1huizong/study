#! /usr/bin/env python
# -*- coding:UTF-8 -*-
# 使用锁的线程

import threading
import time

b = 50

# 增加一个锁对象,锁，在对对象修改时特别有用
l = threading.Lock()

def threadcode():
    global b
    print "Thread %s invoked" % threading.currentThread().getName()

    l.acquire()  # 最主要的是，可以保证一系列的操作是原子的1
    try:
        print "Thread %s running" % threading.currentThread().getName()
        time.sleep(1)
        b = b + 50
        print "Thread %s set b to %d" % (threading.currentThread().getName(),b)
    finally:
        l.release()

print "Value of b at start of program:",b

childthreads = []
for i in xrange(1,5):
    t = threading.Thread(target = threadcode, name = "Thread-%d" % i)
    t.setDaemon(True)
    t.start()
    childthreads.append(t)

for thread in childthreads:
    thread.join()

print "New value of b:",b
