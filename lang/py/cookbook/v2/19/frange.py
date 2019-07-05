#! /usr/bin/env python
# -*-coding:UTF-8 -*-

import itertools
import math

# xrange的float版本

def frange(start, stop=None, inc=1.0):
    if stop is None:
        stop = start + 0.0
        start = 0.0
    assert inc
    for i in itertools.count():
        next_item = start + i * inc
        if (inc>0.0 and next_item >= stop) or (inc<0.0 and  next_item <= stop):
            break
        yield next_item

def frange1(start, stop=None, inc=1.0):
    if stop is None:
        stop = start + 0.0
        start = 0.0
    nitems = int(math.ceil((stop - start)/inc))  # 项数
    for i in xrange(nitems):
        yield start + i * inc
