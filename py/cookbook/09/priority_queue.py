#! /usr/bin/env python
# -*- coding:UTF-8 -*-

import Queue, heapq, time

class PriorityQueue(Queue):
    
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.queue = []

    def _qsize(self):
        return len(self.queue)

    def _empty(self):
        return not self.queue

    def _full(self):
        return self.maxsize > 0 and len(self.queue) >= self.maxsize

    def _put(self, item):
        heapq.heappush(self.queue, item)

    def _get(self):
        return heapq.heappop(self.queue)

    def put(self, item, priority=0, block=True, timeout=None):
        decorated_item = priority, time.time(), item
        Queue.Queue.put(self, decorated_item, block, timeout)

    def get(self, block=True,  timeout=None):
        priority, time_posted, item = Queue.Queue.get(self, block,timeout)
        return item





