#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
def upper_attr(cls,parents,attrs):
    attrs = (  (name,value) for name, value in attrs.items() if not name.startswith('__') )
    upper_attrs = dict( (name.upper(),value )  for name,value in attrs)
    return type(cls,parents,upper_attrs)
"""


# 自定义元类
class UpperAttrMetaclass(type):
    def __new__(cls,name,bases,dit):
        attrs = (  (name,value) for name, value in dit.items() if not name.startswith('__') )
        upper_attrs = dict( (name.upper(),value )  for name,value in attrs)
        return super(UpperAttrMetaclass,cls).__new__(cls,name,bases,upper_attrs)

# 使用元类
__metaclass__ = UpperAttrMetaclass

class Foo:
    bar = 'bip'

print hasattr(Foo,'bar')
print hasattr(Foo,'BAR')

f = Foo()
print f.BAR
