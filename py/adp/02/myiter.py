#!/usr/bin/env python
# -*- coding:utf-8  -*-

# 实现了迭代器协议的类
class MyIter1(object):
    def __init__(self,step):
        self.step = step

    def next(self):
        if self.step == 0:
            raise StopIteration
        self.step  -= 1
        return self.step
    
    def __iter__(self):
        return self

class MyIter2(object):
    def __init__(self,step):
        self.step = step

    def next(self):
        """ 
        实现的效果是step,step-1,...,0 
        """
        if self.step == 0:
            raise StopIteration
        self.step  -= 1
        return self.step
    def __iter__(self):
        return self

def test():
    for  el in MyIter1(4):
        print el
    for el in MyIter2(4):
        print el

if __name__ == '__main__':
    test()
