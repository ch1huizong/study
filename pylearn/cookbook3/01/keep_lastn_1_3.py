#! /usr/bin/env python3
# -*-coding:UTF-8 -*-
# @Time    : 2018/12/24 18:47:34
# @Author  : che
# @Email   : ch1huizong@gmail.com

from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


if __name__ == '__main__':
    with open('somefile.txt') as f:
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-' * 20)
