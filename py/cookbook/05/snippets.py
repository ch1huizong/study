#!/usr/bin/env python
# -*- coding:utf-8  -*-

# 如果子项目是列表和元组就展开
def list_or_tuple(item):
    if isinstance(item,(list,tuple)):
        return True
    else:
        return False

# 如果子项目是非字符串的可迭代项目则展开
def no_string_iter(item):
    try:
        iter(item)
    except TypeError:
        return False
    else:
        return not isinstance(item,basestring)


def flatten(seq,predict=list_or_tuple):
    """
    延展函数,可以选择断言
    """
    for item in seq:				
        if predict(item):
            for subitem in flatten(item,list_or_tuple):    # 这里重要
                yield subitem
        else:
            yield item

def pick_and_reorder_cols(listofRows, col_indexes):
    """
    选取二维列表特殊的列并重排
    """
    return [ [ row[c] for c  in col_indexes  ]  for row in listofRows ]

def addword(theIndex,word,pagenumber):
    """
    theIndex是字典，尤其对字典的值是列表特别有用；
    如果有word,增加到索引字典；
    没有建立一个空列表
    """
    theIndex.setdefault(word,[]).append(pagenumber)


# 产生(key,value)对
def pairwise(iterable):
    itnext = iter(iterable).next
    while True:
        yield itnext(), itnext()		

def dictFromSeq(seq):
    """
    交替使用可迭代容器中的元素作为键和值创建字典
    """
    return dict(pairwise(seq))
