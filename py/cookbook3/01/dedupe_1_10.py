#! /usr/bin/env python3
# -*-coding:UTF-8 -*-
# @Time    : 2018/12/25 17:30:47
# @Author  : che
# @Email   : ch1huizong@gmail.com
# 去重并保持顺序


def dedupe(items):  # for hashable item
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


def dedupe1(items, key=None):  # unique函数, for unhashable item
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


if __name__ == '__main__':
    a = [1, 5, 2, 1, 9, 1, 5, 10]
    print(list(dedupe(a)))

    a = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3},
         {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
    print(list(dedupe1(a, key=lambda d: (d['x'], d['y']))))
    print(list(dedupe1(a, key=lambda d: d['x'])))
