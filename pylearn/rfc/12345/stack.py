#!/usr/bin/env python
# -*-coding:UTF-8 -*-


class Stack(object): 

    def __init__(self):
        self.stack = []

    def push(self,object):
        self.stack.append(object)

    def pop(self):
        return self.stack.pop()

    def length(self):
        return len(self.stack)


class Stack1(list):

    #为栈接口提供push方法
    def push(self,object):
        self.append(object)
