#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 老版本
class Foo1(object):

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

    name = property(getname,setname,delname)

# 新版本
class Foo2(object):
    def __init__(self,name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,value):
        if not isinstance(value,str):
            raise TypeError("Must be a string!")
        self.__name = value

    @name.deleter
    def name(self):
        raise TypeError("Can't delete name")


