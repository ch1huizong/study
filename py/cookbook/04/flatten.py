#! /usr/bin/env python
# -*- coding:UTF-8

def list_or_tuple(x):   #判定函数
    return isinstance(x, (list, tuple))

def nonstring_iter(obj): #非字符串的可迭代对象
    try:
        iter(obj)
    except TypeError:
        return Fasle
    else:
        return not isinstance(obj, basestring)

def flatten(seq, to_expand = list_or_tuple):
    for item in seq:
        if to_expand(item):
            for subitem in flatten(item, to_expand):  #递归
                yield subitem
        else:
            yield item

def flatten_no(seq, to_expand = list_or_tuple):  #非递归版本
    iters = [ iter(seq) ]   # 使用了一个数据结构，栈
    while iters:
        for item in iters[-1]:  # 最新加入的迭代器
            if to_expand(item):
                iters.append(iter(item))
                break  # 停止本次的迭代，进入新插入的迭代器
            else:
                yield item
        else:
            iters.pop() # 新插入的迭代器使用完成
    
