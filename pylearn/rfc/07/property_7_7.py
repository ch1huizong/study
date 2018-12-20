# -*- coding:utf-8 -*-
import math


class Circle(object):

    # 限制可以访问的实例属性名称
    __slots__ = ('radius','age')
    
    def __init__(self,radius):
        self.radius = radius
    
    @property
    def area(self): # n1
        return math.pi*self.radius**2

    @property
    def perimeter(self):
        return 2*math.pi*self.radius

    def __getattr__(self, name):

        if name == 'area': # n2    n1还是n2优先？ n1优先
            print('n2 优先')
            return math.pi * self.radius ** 2
        elif name == 'perimeter':
            return 2 * math.pi * self.radius
        else:
            return object.__getattr__(self, name)

    def __setattr__(self, name, value):
        if name in ['area', 'perimeter']:
            raise TypeError("%s is readonly"%name)
        object.__setattr__(self, name, value)  # 隔离发挥作用了


# 老版本
class OldFoo(object):

    def __init__(self,name):
        self.__name = name

    def getname(self):
        return self.__name
    
    def setname(self,value):
        if not isinstance(value,str):
            raise TypeError("Must be a string!")
        self.__name = value

    def delname(self):
        raise TypeError("Can't delete name")

    name = property(getname, setname, delname)


# 新版本
class Foo(object):
    
    def __init__(self,name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value,str):
            raise TypeError("Must be a string!")
        self.__name = value

    @name.deleter
    def name(self):
        raise TypeError("Can't delete name")
