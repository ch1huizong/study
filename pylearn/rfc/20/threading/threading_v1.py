#!/usr/bin/env python
# -*- coding:UTF-8 -*-

import threading
import time

def clock(interval):
    while True:
        print'The time is %s' % time.ctime()
        time.sleep(interval)

t = threading.Thread(target=clock,args=(5,))
t.daemon = True
t.start()

"""
#为了验证daemon的效果
for i in range(10):
    print i
    time.sleep(1)
"""
