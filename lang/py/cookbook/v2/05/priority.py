#! /usr/bin/env python
# -*- coding:UTF-8 -*-

import heapq

class prioq(object):   # 优先级队列,nice
    def __init__(self):
        self.q = [  ]
        self.i = 0
    
    def push(self, item, cost):
        heapq.heappush(self.q, (-cost, self.i, item))
        self.i += 1

    def pop(self):
        return heapq.heappop(self.q)[-1]
