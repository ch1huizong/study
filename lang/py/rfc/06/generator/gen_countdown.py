#!/usr/bin/env python
# -*- coding:utf-8 -*-

def countdown(n):
    print("Counting down from  %d" % n)
    try:
        while n > 0:
            yield n
            n -= 1
    except GeneratorExit: # 捕获GeneratorExit异常
        print("Only made it to %d" % n)
