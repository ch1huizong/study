#!/usr/bin/env python
# -*- coding:UTF-8 -*-

import threading
import time


class Clock(threading.Thread):

    def __init__(self, interval):
        threading.Thread.__init__(self)
        self.daemon = True
        self.interval = interval

    def run(self):
        while True:
            print('The time is %s' % time.ctime())
            time.sleep(self.interval)


t = Clock(2)
t.start()
