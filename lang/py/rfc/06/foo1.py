#!/usr/bin/env python
# -*- coding:UTF -*-

x = 42

def callf(func): #本身也有环境
    print("callf本身的x is %d" % x)
    return func()
