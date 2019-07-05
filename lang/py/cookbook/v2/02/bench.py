#! /usr/bin/env python
# -*- coding:UTF-8 -*-

import time

def timeo(fun, n=10):
    start = time.clock()
    for i in xrange(n): fun()
    end = time.clock()
    thetime = end - start
    return fun.__name__, thetime

import os

def linecount_wc():
    return int(os.popen('wc -l syslog').read().split()[0])

def linecount_1():
    return len(open('syslog').readlines())

def linecount_2():
    for count, line in enumerate(open('syslog')): pass
    return count + 1

def linecount_3():   # 更具技巧性，统计\n的次数
    count = 0
    thefile = open('syslog', 'rb')
    while True:
        block = thefile.read(65536)
        if not block: break
        count += block.count('\n')
    return count

for f in linecount_wc, linecount_1, linecount_2, linecount_3:
    print f.__name__, f()

for f in linecount_1, linecount_2, linecount_3:
    print "%s: %.2f" % timeo(f)


