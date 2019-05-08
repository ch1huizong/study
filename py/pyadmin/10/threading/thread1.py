#! /usr/bin/env python
# -*- coding:UTF-8 -*-

import threading
import time

count = 1 # 其实会引起竞争问题

class KissThread(threading.Thread):
    def run(self):
        global count
        print "Thread # %s: Pretending to do stuff" % count
        count += 1
        time.sleep(2)
        print "done with stuff"

for t in range(5):
    KissThread().start()
