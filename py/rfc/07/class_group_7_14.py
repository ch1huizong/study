#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Foo(object):
    def spam(self,a,b):
        pass


class FooProxy(object):
    def __init__(self,f):
        self.f = f

    def spam(self,a,b):
        return self.f.spam(a,b)


# 对一些类进行分组
class IClass(object):

    def __init__(self):
        self.implementors = set()

    def register(self, C):
        self.implementors.add(C)

    #　重新定义isinstance方法
    def __instancecheck__(self, x):
        return self.__subclasscheck__(type(x))


    #  重新定义issubclass方法
    def __subclasscheck__(self, sub):
        return any((c in self.implementors) for c in sub.mro())  

        
def test(): 
    IFoo = IClass()
    IFoo.register(Foo)
    IFoo.register(FooProxy)

    f = Foo()
    g = FooProxy(f)
    print(isinstance(f,IFoo))
    print(isinstance(g,IFoo))
    print(issubclass(FooProxy,IFoo))

test()
