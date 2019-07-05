#! /usr/bin/env python
# -*- coding:UTF-8 -*-
# 死锁,就是线程互相等待相互的资源，互不想让,本质相互依赖

import threading
import time

a = 5
alock = threading.Lock()
b = 5
block = threading.Lock()

def thread1calc():
    print "Thread1 acquiring lock a"
    alock.acquire()
    time.sleep(5)

    print "Thread1 again attempt acquiring lock b"
    block.acquire()
    time.sleep(5)
    a += 5
    b += 5

    print "Thread1 releasing both locks"
    block.release()
    alock.release()

def thread2calc():
    print "Thread2 acquiring lock b"
    block.acquire()
    time.sleep(5)

    print "Thread2 again attempt acquiring lock a"
    alock.acquire()    #这里就僵死了吧,hahah
    time.sleep(5)
    a += 10
    b += 10

    print "Thread2 releasing both locks"
    block.release()
    alock.release()

t = threading.Thread(target = thread1calc)
t.setDaemon(True)
t.start()

t = threading.Thread(target = thread2calc)
t.setDaemon(True)
t.start()

while True:
    time.sleep(300)

