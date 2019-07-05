#! /usr/bin/env python3
# -*-coding:utf-8 -*-
# @Time    : 2019/06/16 17:25:29
# @Author  : che
# @Email   : ch1huizong@gmail.com

from threading import Timer
import sys
import time
import copy

if len(sys.argv) != 2:
    print("Must enter an interval")
    sys.exit(1)


def hello():
    print("Hello, I just got called after a %s sec delay" % call_time)


delay = sys.argv[1]
call_time = copy.copy(delay)
delay = int(delay)
t = Timer(delay, hello)  # 可以当作一个延迟线程
t.start()

print("waiting %s seconds to run function" % delay)
for x in range(delay):
    print("Main program is still running for %s more sec" % delay)
    delay -= 1
    time.sleep(1)
