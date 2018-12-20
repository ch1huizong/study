#!/usr/bin/env python 
# -*- coding:UTF-8 -*-
#
# shutdownevt.py
#
# Example of a generator that uses an event to shut down

import time

def follow(thefile,shutdown=None):
    thefile.seek(0,2)
    while True:
        # 通过设置一个"全局"标志位，来关闭生成器
        if shutdown and shutdown.isSet(): break  # 从内部关闭
        line = thefile.readline()
        if not line:
           time.sleep(0.1)
           continue
        yield line


import threading
shutdown_event = threading.Event()

def run():
    lines = follow(open("run/foo/access-log"),shutdown_event)
    for line in lines:
        print line,

    print "Done"

# Run the above in a separate thread
t = threading.Thread(target=run)
t.start()

# Wait a while then shut down
time.sleep(60)
print "Shutting down"

shutdown_event.set()
