#!/usr/bin/env python 
# -*- coding:UTF-8 -*-
#
# genpickle.py
#
# Turn a sequence of objects into a sequence of pickle strings

import pickle

def gen_pickle(source): 
    for item in source:
        yield pickle.dumps(item) # 把每一个项目变成pickled字符串

def gen_unpickle(infile): # 如若文件
    while True:
        try:
            item = pickle.load(infile) # 每次从pickled文件载入一条数据
            yield item
        except EOFError:
            return
