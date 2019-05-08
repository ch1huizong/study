#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#
# bogus.py
# 
# 既产生值又接收值的生成器, 不好
# Bogus example of a generator that produces and receives values

def countdown(n):
    print "Counting down from", n
    while n >= 0:
        newvalue = (yield n)
        # If a new value got sent in, reset n with it
        if newvalue is not None:
            n = newvalue
        else:
            n -= 1

# The holy grail countdown
c = countdown(5)
for x in c: 
    print x
    if x == 5:
        c.send(3)  # 本次迭代淹没3
