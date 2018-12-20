#!/usr/bin/env python
# encoding: UTF-8

import threading,time

l=threading.Lock()

def worker():
    l.acquire()
    print threading.currentThread().getName(),'Starting'
    time.sleep(2)
    print threading.currentThread().getName(),'Exiting'
    l.release()

def my_service():
    l.acquire()
    print threading.currentThread().getName(),'Starting'
    time.sleep(3)
    print threading.currentThread().getName(),'Exiting'
    l.release()

t=threading.Thread(name='My_service',target=my_service)
w=threading.Thread(name='worker',target=worker)
wd=threading.Thread(target=worker)

t.start()
w.start()
wd.start()
    
