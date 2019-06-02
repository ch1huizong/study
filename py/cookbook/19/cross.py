#! /usr/bin/env python
# -*- coding:UTF-8 -*-

# 矢量积
def cross_loop(*sequences):
    if sequences:
        for x in sequences[0]:
            for y in cross_loop(sequences[1:]):
                yield (x,) + y
    else:
        yield ()

def cross_list(*sequences):
    result = [ [] ]
    for seq in sequences:
        result = [ sublist + [item] for sublist in result for item in seq ] #太他妈巧妙了!
    return result

def cross(*sequences):
    wheels = map(iter, sequences)  # 保存迭代器
    digits = [ it.next() for it in wheels]  # 保存子项结果
    while True:
        yield tuple(digits)
        for i in range(len(digits)-1,-1,-1): # 从后往前选择迭代器
            try:
                digits[i] = wheels[i].next() # 改变最后一项(迭代器对应的元素)
                break
            except StopIteration:
                wheels[i] = iter(sequences[i])  # 恢复并复位
                digits[i] = wheels[i].next()
        else:
            break

