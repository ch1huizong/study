#!/usr/bin/env python
# -*- coding:UTF-8 -*_
#
# cocrash.py
#
# An example of hooking coroutines up in a way that might cause a potential
# crash.   Basically, there are two threads feeding data into the
# printer() coroutine.    
#
# 问题就是： thread1正send, thread2也开始send

from cobroadcast import *
from cothread import threaded

# 两个线程同时引用一个target,send,可能target正处理先来的线程发送的数据!
p = printer() 
target = broadcast([threaded(grep('foo',p)),  
                    threaded(grep('bar',p))])

# Adjust the count if this doesn't cause a crash
for i in xrange(10):
    target.send("foo is nice\n")
    target.send("bar is bad\n")

del target
del p
