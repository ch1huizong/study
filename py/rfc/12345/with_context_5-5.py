#! /usr/bin/env python3
# -*- coding:UTF-8 -*-


# 列表事务
class ListTransaction(object):

    def __init__(self,thelist):
        self.thelist = thelist

    def __enter__(self):
        self.workingcopy = list(self.thelist)
        return self.workingcopy 

    def __exit__(self,type,value,tb):
        if type is None: 
            self.thelist[:] = self.workingcopy
        return False


# 通过函数定义上下文管理器
from contextlib import contextmanager
@contextmanager
def ListTransaction1(thelist):
    workingcopy = list(thelist)
    yield workingcopy
    thelist[:] = workingcopy


def test():
    items = [1,2,3]
    print("改变前:", items)
    with ListTransaction(items) as working:
        working.append(4)
        working.append(5)
    print("改变后:", items)


    try:
        with ListTransaction(items) as working:
            working.append(6)
            working.append(7)
            raise RuntimeError("We're hosed!")
    except RuntimeError:
            pass
    print("类版本,未变化:" ,items)

    try:
        with ListTransaction1(items) as working:
            working.append(6)
            working.append(7)
            raise RuntimeError("We're hosed!")
    except RuntimeError:
            pass
    print("装饰器版本,未变化:" ,items)

test()
