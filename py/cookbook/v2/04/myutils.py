#! /usr/bin/env  python
# -*- coding:UTF-8 -*-
# 一些比较好的代码片段

def pick_and_reorder_columns(listofRows, column_indexes):
    return [ [row[ci] for ci in column_indexes ] for row in listofRows ]

def pairwise(iterable):
    iternext = iter(iterable).next()
    while True:
        yield itnext(),itnext()

def dictFromSeq(seq):
    return dict(pairwise(seq))
