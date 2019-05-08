#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
# 使用协程完成多线程的任务


from collections import deque


def foo():
    for n in range(5):
        print("I'm foo %d" % n)
        yield


def bar():
    for n in range(10):
        print("I'm bar %d" % n)
        yield


def spam():
    for n in range(7):
        print("I'm spam %d" % n)
        yield


taskqueue = deque()
taskqueue.append(foo())
taskqueue.append(bar())
taskqueue.append(spam())

while taskqueue:  # 任务调度
    task = taskqueue.pop()
    try:
        task.__next__()
        taskqueue.appendleft(task)
    except StopIteration:
        pass
