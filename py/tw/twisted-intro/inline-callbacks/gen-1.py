# -*- coding:utf-8 -*-


def my_generator():
    print "starting up"
    yield 1
    print "workin'"
    yield 2
    print "still workin'"
    yield 3
    print "done"


for n in my_generator(): # 自己处理的迭代异常了
    print n
