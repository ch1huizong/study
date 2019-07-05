#! /usr/bin/env python 
# -*- coding:UTF-8 -*-

import random

def select(data, n):
    """
    取的排名第n的最小元素，最小的是第0号元素
    序列很长，而且比较操作比较耗时，新方法时间复杂度O(n)
    """
    data = list(data)
    if n < 0:
        n += len(data)
    if not 0<= n < len(data):
        raise ValueError, "can'nt get rank %d out for %d" % (n, len(data))

    ###很类似快速排序，但丢弃片段，不递归
    while True:
        pivot = random.choice(data)
        pcount = 0
        under , over = [], []
        uappend, oappend = under.append, over.append 
        for e in data:
            if e < pivot:
                uappend(e)
            elif e > pivot:
                oappend(e)
            else:
                pcount += 1
        number = len(under)
        if n < number:
            data = under
        elif n < number + pcount:
            return pivot
        else:
            data = over
            n -= number + pcount
     
