#! /usr/bin/env python
# -*- coding:UTF-8 -*-

# 获得一个可迭代对象的前arg_cnt项，
# 赋值， 余下的部分不变
def peel(iterable, arg_cnt=1):
    iterator = iter(iterable)
    for num in xrange(arg_cnt):
        yield iterator.next()
    yield iterator

if __name__ == '__main__':
    t5 = range(1,6)
    a, b, c  = peel(t5, 2)  # a, b, *c = t 新语法
    print a, b, list(c)





