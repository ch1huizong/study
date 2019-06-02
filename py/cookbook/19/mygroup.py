#! /usr/bin/env python
# -*- coding:UTF-8 -*-

# groupby
class groupby(dict):
    def __init__(self, seq, key):
        for row in seq:
            k = key(row)
            self.setdefault(k, []).append(row)
    __iter__ = dict.iteritems

# 偏函数
def itemgetter(i):
    def getter(x):
        return x[i]
    return getter

# DSU算法
def mysorted(seq, key):
    aux = [ (key(x), i, x) for i, x in enumerate(seq) ]
    aux.sort()
    return [ x for k, i, x in aux ]

