#!/usr/bin/env python
# -*- coding:UTF-8 -*-

import threading
import time

event=threading.Event()

def func():
    #等待事件，进入等待阻塞状态
    print'%s wait for event...'%threading.currentThread().getName()
    event.wait()

    #收到事件后进入运行状态
    print'%s recv event.'% threading.currentThread().getName()

t1=threading.Thread(target=func)
t2=threading.Thread(target=func)
t1.start()
t2.start()

time.sleep(2)

#发送事件通知
print'MainThread set event.'
event.set()
