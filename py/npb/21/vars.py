#! /usr/bin/env python
# -*- coding:UTF-8 -*-

import threading
import time

a = 50
b = 50
c = 50
d = 50

def printvars():
    print "a = ", a
    print "b = ", b
    print "c = ", c
    print "d = ", d

def threadcode():
    global a, b, c, d  # 引用全局变量
    a += 50
    b = b + 50
    c = 100
    d = "Hello"
    print "[Child Thread] Values of variables in child thread:"
    printvars()

print "[Main Thread] values of variables before child thread:"
printvars()

t = threading.Thread(target = threadcode, name = "Child Thread")
t.setDaemon(1)
t.start()
t.join()

print "[Main Thread] values of variables after child thread:"
printvars()

