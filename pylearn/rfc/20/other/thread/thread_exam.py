#!/usr/bin/env python
# encoding: UTF-8

import thread
import time

def func():
    for i in range(5):
        print'func'
        time.sleep(1)

    thread.exit()

thread.start_new(func,())

lock=thread.allocate()
print lock.locked()

count=0

if lock.acquire():
    count+=1

    lock.release()

time.sleep(6)

