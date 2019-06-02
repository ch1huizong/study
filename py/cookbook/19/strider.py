#! /usr/bin/env python
# -*- coding:UTF-8 -*-

import itertools

def strider(p, n):   # 最通用
    result = [ [] for i in xrange(n) ]

    for i, item in enumerate(p):   # 关注点，所有的元素
        result[i % n].append(item)  # 有点技巧
    return  result

# 都要求是序列
def strider1(p, n):
    return [ list(p[i::n])  for i in xrange(n)]

def strider2(p, n):
    for i in xrange(n):
        yield p[i::n]

def strider3(p, n):
    return itertools.imap(lambda i: p[i::n], xrange(n))

def strider4(p, n):
    return (p[i::n] for i in xrange(n))

# 同最上,不用索引了
def strider(p, n):
    result = [ [] for i in itertools.repeat(0,n) ]
    resister = itertools.cycle(result)   # 无穷循环迭代器
    for item, sublist in itertools.izip(p, resister): # 关注点子列表
        sublist.append(item)
    return result

# 滑动窗口, ...|...|...|...
def windows(iterable, length=2,  overlap=0):
    # import collections
    it = iter(iterable)
    results = list(itertools.islice(it, length))  # 第一个窗口
    while len(results) == length:
        yield results
        results = results[length-overlap:]  # 重合的部分，开始索引 
        # 优化1，del results[:length-overlap],这样就使用同一个列表了
        # 优化2, for i in xrange(length-overlap): results.popleft()
        results.extend(list(itertools.islice(it, length-overlap))) # 持续调用
    if results:
        yield results



# WOW! 太厉害了！izip(it,it...) it 都是引用的同一个迭代器
# izip驱动第一个迭代器里第一项，第二个迭代器(同一个)里下一项...
def chop(iterable, length=2):
    return  itertools.izip(*(iter(iterable),)*length)



if __name__ == '__main__':
    seq = 'foobarbazer'
    for length in (3, 4):
        for overlap in (0, 1):
            print "%d %d:   %s"%(length, overlap,
                    map(''.join, windows(seq, length, overlap)))
