#!/usr/bin/env python
# encoding: UTF-8

import threading
import time

def worker():
    print threading.currentThread().getName(),'starting'
    time.sleep(3)
    print threading.currentThread().getName(),'ending'

d=threading.Thread(target=worker)
d.setDaemon(True)

t=threading.Thread(target=worker)

d.start()
t.start()
print'Main-Thread Over'
