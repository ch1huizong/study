#! /usr/bin/env python
# -*- coding:UTF-8 -*-

"""
    Perl或者C语言中赋值并测试语句的代码翻译
    制作了一个中间对象
"""

class DataHolder(object):
    def __init__(self,value=None):
        self.value = value
    def set(self,value):
        self.value = value
        return self.value
    def get(self):
        return self.value

import __builtin__
__builtin__.DataHolder = DataHolder
__builtin__.data = data = DataHolder()

# 模拟的下面这个语句
# while( line = f.readline() != '' )
#    process(line)

while data.set(f.readline()) != '': 
    process(data.get())

