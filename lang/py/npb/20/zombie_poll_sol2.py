#! /usr/bin/env python
# -*- coding:UTF-8 -*-
# 利用轮循解决zombie问题
# 问题：需要不停的检查收割？

import os
import time

def reap():
    """Try to collect zombie processes, if any..."""
    while True:
        try:
            result = os.waitpid(-1,os.WNOHANG)  # 收割
        except:
            break
        print "Reaped child process %d"%result[0]



print "Before the fork, my PID is" ,os.getpid()

pid = os.fork()

if pid:
    print "Hello from the parent. The child will be PID %d" % pid
    print "Sleeeping 60 second..."
    time.sleep(60)
    print "Parent Sleep done."
    reap() # 检查一次，收割
    print "Sleeeping 60 second..."
    time.sleep(60)
    print "Parent sleep done."
else:
    print "Child sleeping 5 seconds..."
    time.sleep(5)
    print "Child terminating."

