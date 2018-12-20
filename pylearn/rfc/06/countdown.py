#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 定义嵌套函数v1
def countdown1(start):
    n = start
    def display():
        print("T-mimus %d"%n)
    while n > 0:
        display()
        n -= 1


def countdown2(start):
    n = start
    def display():
        print("T-mimus %d"%n)

     # 下面的语句在python2/3中不起作用,只能访问，
     # 不能修改"外部函数"中的局部变量n
    def decrement():
        n -= 1

    while n > 0:
        display()
        decrement()


#解决内部函数修改外部函数变量的行为
def countdown3(start):
    n = start
    def display():
        print("T-mimus %d"%n)
    
    def decrement():
        nonlocal n  # 声明nonlocal,只在python3中有效
        n -= 1

    while n > 0:
        display()
        decrement()


# v1计数器,验证闭包,闭包用于保存内部计数器的值n
def countdown4(n):
    def next():
        nonlocal n
        r = n
        n -= 1
        return r
    return next


# v2用一个类来实现闭包类似的功能
class Countdown(object):

    def __init__(self,n):
        self.n = n

    def next(self):
        r = self.n
        self.n  -= 1
        return r
