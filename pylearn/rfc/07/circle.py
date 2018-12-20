#!/usr/bin/env python
# -*- coding:utf-8 -*-

import math

class Circle(object):

    # 限制可以访问的实例属性名称
    __slots__ = ('radius','age')
    
    def __init__(self,radius):
        self.radius = radius
    
    @property
    def area(self):  #note1  本质上是方法
        return math.pi*self.radius**2
    @property
    def perimeter(self):
        return 2*math.pi*self.radius

    #重定义属性访问操作
    def __getattr__(self,name):
        if name == 'area': #note2    note1还是note2优先？ note1优先
            print "note2 优先"
            return math.pi*self.radius**2
        elif name == 'perimeter':
            return 2*math.pi*self.radius
        else:
            return object.__getattr__(self,name)

    def __setattr__(self,name,value):
        if name in ['area','perimeter']:
            raise TypeError("%s is readonly"%name)
        object.__setattr__(self,name,value)  # 隔离发挥作用了

