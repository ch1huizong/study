#! /usr/bin/env python
# -*- coding:UTF-8 -*-

from multiprocessing import Process, Queue
import time

def f(q):
    x = q.get()
    print "Process number %s, sleeps for %s seconds" % (x, x) # 自己定义的进程号码
    time.sleep(x)
    print "Process number %s finished" % x

q = Queue()

for i in range(10):
    q.put(i)
    i = Process(target=f, args=[q]) # 假设，当前开启的进程会立刻处理传到“队列”的项目
    i.start()

print "main process joins on queue"
i.join()
print "Main Program finished"
