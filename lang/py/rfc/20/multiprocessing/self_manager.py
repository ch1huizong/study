#!/usr/bin/env python

import multiprocessing
from multiprocessing.managers import BaseManager

class A(object):

    def __init__(self,value):
        self.x = value
        
    def __repr__(self):
        return'A(%s)'%self.x

    def getX(self):
        return self.x

    def setX(self,value):
        self.x = value

    def __iadd__(self,value):
        self.x += value
        return self

class MyManager(BaseManager):
    pass

MyManager.register("A",A)

if __name__ == '__main__':
    m = MyManager()
    m.start()
    a = m.A(37)
