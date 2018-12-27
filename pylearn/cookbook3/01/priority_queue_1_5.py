#! /usr/bin/env python3
# -*-coding:UTF-8 -*-
# @Time    : 2018/12/25 11:37:57
# @Author  : che
# @Email   : ch1huizong@gmail.com
# 为何先heapify? heap头序

import heapq


class PriorityQueue(object):
    
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        # 注意构造item顺序, 以heapq的规则插入项目
        heapq.heappush(self._queue, (-priority, self._index, item)) 
        self._index += 1

    def pop(self):
        # 以heapq的规则取出项目
        return heapq.heappop(self._queue)[-1]


class Item(object):

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)


if __name__ == '__main__':
    q = PriorityQueue()
    q.push(Item('foo'), 1)
    q.push(Item('bar'), 5)
    q.push(Item('spam'), 4)
    q.push(Item('grok'), 1)
    
    for __ in range(4):
        print(q.pop())
