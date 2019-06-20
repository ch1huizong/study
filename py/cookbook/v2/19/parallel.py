#! /usr/bin/env python
# -*- coding:UTF-8 
# 并行处理可迭代对象

import itertools

# 只是两个序列
def par_two(a, b, padding_item=None):
    a, b = iter(a), iter(b)
    for item in itertools.izip(a,b):
        yield item
    for item in a:
        yield item, padding_item
    for item in b:
        yield padding_item, item

# 更通用,多个序列,关键是转化
def par_loop(padding_item, *sequences):
    iterators = map(iter,sequences)  # 保存多个迭代器
    num_remaining = len(iterators)
    result = [ padding_item ] * num_remaining # 临时列表
    while num_remaining:
        for i, it in enumerate(iterators):
            try:
                result[i] = it.next()
            except StopIteration:
                iterators[i] = itertools.repeat(padding_item)  # 变一个迭代器
                result[i] = padding_item
                num_remaining -= 1
        if num_remaining:
            yield tuple(result)

# 只有第一个迭代器是最长的
def par_longest_first(padding_item, *sequences):
    iterators = map(iter, sequences)
    for i, it in enumerate(iterators):
        if not i:
            continue
        iterators[i] = itertools.chain(it, itertools.repeat(padding_item))
    return itertools.izip(iterators)

if __name__ == '__main__':
    print map(''.join, par_loop('x','foo','zapper','ui'))

