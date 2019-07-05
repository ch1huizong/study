#! /usr/bin/env python
# -*- coding:UTF-8 -*-

"""
    序列item的项的数目不确定，但现在要求有n个不同的
    坑，用items集合里的东西填充。
"""

# 排列组合
def _combinators(_handle, items, n):
    """base"""
    if n == 0:
        yield []
        return
    for i, item in enumerate(items):
        this_one = [ item ]  # 可以改为元组 this_one = item,或者与items相同的类型
        for cc in _combinators(_handle, _handle(items, i), n-1): # 递归
            yield this_one + cc

def combinations(items, n):
    """取得n个不同的项，顺序是有意义的"""
    def skipTheItem(items, i):
        return items[:i] + items[i+1:] 
    return _combinators(skipTheItem, items, n)

def uniqCombinations(items, n):
    """取得n个不同的项，顺序无关"""
    def afterTheItem(items, i):
        return items[i+1:]    # 不要有前面出现过的项
    return _combinators(afterTheItem, items, n)

def selections(items, n):
    """取得n项(不一定不同),顺序有意义"""
    def keepAllItems(items, i):
        return items
    return _combinators(keepAllItems, items, n)

def permutations(items):
    """取得所有项，顺序是有意义的"""
    return combinations(items, len(items))

if __name__ == '__main__':
    print 'Permutations of "bar"'
    print map(''.join, permutations('bar'))
    print 
    print 'Combinations of 2 letters from "bar"'
    print map(''.join, combinations('bar',2))
    print
    print 'UniqCombinations of 2 letters from "bar"'
    print map(''.join, uniqCombinations('bar',2))
    print
    print 'Selections of 2 letters from "bar"'
    print map(''.join, selections('bar',2))


