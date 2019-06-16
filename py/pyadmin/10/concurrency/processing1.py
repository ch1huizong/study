#! /usr/bin/env python3
# -*-coding:utf-8 -*-
# @Time    : 2019/06/16 18:52:49
# @Author  : che
# @Email   : ch1huizong@gmail.com

from multiprocessing import Process, Queue
import time


def f(q):
    x = q.get()
    print("Process number %s, sleeps for %s seconds" % (x, x))
    time.sleep(x) # 若time.sleep(10-x)
    print("Process number %s finished" % x)


q = Queue()

for i in range(10):
    q.put(i)
    i = Process(target=f, args=[q])
    i.start()

print("main process joins on queue")
i.join() # 其实可以没有
print("Main Program finished")
