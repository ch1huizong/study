#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# 使用协程完成多线程的任务

def foo():
    for n in xrange(5):
        print"I'm foo %d"%n
        yield

def bar():
    for n in xrange(10):
        print"I'm bar %d"%n
        yield

def spam():
    for n in xrange(7):
        print"I'm spam %d"%n
        yield

from collections import deque
taskqueue = deque()
taskqueue.append(foo())
taskqueue.append(bar())
taskqueue.append(spam())

while taskqueue:  # 任务调度
    #获得下一个任务
    task = taskqueue.pop()
    try:
        #运行它直到下一条yield和enqueue语句
        next(task)
        taskqueue.appendleft(task)
    except StopIteration:
        pass
