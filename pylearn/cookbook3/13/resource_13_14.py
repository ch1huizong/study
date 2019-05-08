#! /usr/bin/env python3
# -*-coding:UTF-8 -*-
# @Time    : 2019/01/05 14:34:41
# @Author  : che
# @Email   : ch1huizong@gmail.com

import signal
import resource
import os


def time_exceeded(signo, frame):
    print('Time\'s up!')
    raise SystemExit(1)


def set_max_runtime(seconds):
    soft, hard = resource.getrlimit(resource.RLIMIT_CPU)
    resource.setrlimit(resource.RLIMIT_CPU, (seconds, hard))
    signal.signal(signal.SIGXCPU, time_exceeded)


def limit_memory(maxsize):
    soft, hard = resource.getrlimit(resource.RLIMIT_AS)
    resource.setrlimit(resource.RLIMIT_AS, (maxsize, hard))


if __name__ == '__main__':
    set_max_runtime(15)
    while True:
        pass
