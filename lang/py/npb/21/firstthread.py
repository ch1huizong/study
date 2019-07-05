#! /usr/bin/env python
# -*- coding:UTF-8 -*-

import time
import threading
import sys

def sleepandprint():
    time.sleep(5)
    print "Hello from both of us."

def threadcode():
    sys.stdout.write("Hello from the new thread.My name is %s\n"%\
            threading.currentThread().getName())
    sleepandprint()

print "Before starting a new thread,my name is",threading.currentThread().getName()

t = threading.Thread(target = threadcode, name = "ChildThread")
# 设置守护进程，主线程若提前终止，子线程也会终止。 
t.setDaemon(1)  
t.start()

sys.stdout.write("Hello from the main thread.My name is %s\n"%\
             threading.currentThread().getName())
sleepandprint()

t.join() # 等待子线程退出,主线程不必非要收割子线程

print "The is a test line..."
time.sleep(2)
print "Now the main thread exit."
