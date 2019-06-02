#! /usr/bin/env python
# -*- coding:UTF-8 -*-

import collections
import itertools

def tee1(iterable):
    def yield_with_cache(next, cache={}): # cache只对相邻的一次迭代起作用？
        pop = cache.pop
        for i in itertools.count():
            try:
                yield pop(i)
            except KeyError:
                cache[i] = next()
                yield cachep[i]
    it = iter(iterable)
    return yield_with_cache(it.next), yield_with_cache(it.next)

def tee2(iterable):
    def yield_with_cache(it, cache=collections.deque):
        while True:
            if cache:
                yield cache.popleft()
            else:
                result = it.next()
                cache.append(result)
                yield result
    it = iter(iterable)
    return yield_with_cache(it), yield_with_cache(it)



