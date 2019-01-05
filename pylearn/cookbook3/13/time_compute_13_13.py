#! /usr/bin/env python3
# -*-coding:UTF-8 -*-
# @Time    : 2019/01/05 11:31:20
# @Author  : che
# @Email   : ch1huizong@gmail.com

import time


class Timer(object):

    def __init__(self, func=time.perf_counter):
        self.elapsed = 0.0
        self._func = func
        self._start = None

    def start(self):
        if self._start is not None:
            raise RuntimeError('Already started')
        self._start = self._func()

    def stop(self):
        if self._start is None:
            raise RuntimeError('Not started')
        end = self._func()
        self.elapsed += end - self._start   # 总耗时
        self._start = None

    def reset(self):
        self.elapsed = 0.0

    @property
    def running(self):
        return self._start is not None

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, *args):
        self.stop()


def countdown(n):
    while n > 0:
        n -= 1


if __name__ == '__main__':
    with Timer() as t2:
        countdown(100000000)
    print(t2.elapsed)
