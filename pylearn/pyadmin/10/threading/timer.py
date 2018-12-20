#! /usr/bin/env python
# -*- coding:UTF-8 -*-

from threading import Timer
import sys
import time
import copy

if len(sys.argv) != 2:
    print "Must enter an interval"
    sys.exit(1)

def hello():
    print "Hello, I just got called after a %s sec delay" % call_time

delay = sys.argv[1]
call_time = copy.copy(delay)
t = Timer(int(delay), hello)  # 可以当作一个延迟线程
t.start()

print "waiting %s seconds to run function" % delay
for x in range(int(delay)):
    print "Main program is still running for %s more sec" % delay 
    delay = int(delay) - 1 # 指示显示
    time.sleep(1)
