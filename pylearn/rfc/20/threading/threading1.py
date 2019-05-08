#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

import threading
import time


def clock(interval):
    while True:
        print('The time is %s' % time.ctime())
        time.sleep(interval)


t = threading.Thread(target=clock, args=(5,))
t.daemon = True
t.start()
#time.sleep(10)
