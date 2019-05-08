#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#下面我们定义一些递归函数，验证递归的功能
#
# 阶乘 !n
def factorial(n):
    """计算阶乘,例如
        >>> factorial(6) 
        120
        >>> 
    """

    if n <=1 :
        return 1
    else:
        return n * factorial(n-1)


# 延展函数,结构简单紧凑
def flatten(lists):
    for s in lists:
        if isinstance(s,list):
            flatten(s)
        else:
            print(s)


# 延展函数的递归版本
def genflatten(lists):
    for s in lists:
        if isinstance(s,list):
            for item  in genflatten(s):  #! 注意了
                yield item
        else:
            yield s
