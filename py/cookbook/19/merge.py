#! /usr/bin/env python
# -*- coding:UTF-8 -*-

import heapq

# 大数据序列合并,未排好序，只生成当前最小值
# 单纯合并没什么优势啊？
def merge(*subsequences):
    heap = []  # 临时列表
    for seq in subsequences:
        iterator = iter(seq)
        for current_value in iterator:
            heap.append((current_value, iterator))
            break
    heapq.heapify(heap)  # 堆化
    while heap:
        current_value, it = heap[0]
        yield current_value
        for current_value in it:  # 惯用法   # 取得选定迭代器的下一个值
            heapq.heapreplace(heap, (current_value, it)) # 替换删除
            break
        else:
            heapq.heappop(heap)

# 小数据
def merge1(*subsequences):
    sequence = []
    for seq in subsequences:
        sequence.extend(seq)
    sequence.sort()
    return sequence

if __name__ == '__main__':
    r = merge([102,1,50,3,7],[11,2,5,6],[3,3,-2,-3])
    print list(r)
