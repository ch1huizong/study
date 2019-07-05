#! /usr/bin/env python
# -*- coding:UTF-8
# 基于信号处理程序的子进程收割

import os
import time
import signal

def chldhandler(signum, stackframe):
    while True:
        try:
            result = os.waitpid(-1,os.WNOHANG) # 任意进程号，不等待
        except:
            break
        print "Reaped child process %d" % result[0]
    signal.signal(signal.SIGCHLD, chldhandler)  # 重新激活


signal.signal(signal.SIGCHLD, chldhandler)   # 父进程设置

print "Before the fork, my PID is" ,os.getpid()

pid = os.fork()

if pid:
    print "Hello from the parent. The child will be PID %d" % pid
    print "Sleeeping 10 second..."
    time.sleep(10)             # 等子进程时间到被收割后，sleep会失效，父进程打印后结束
    print "Parent Sleep done."
else:
    print "Child sleeping 5 seconds..."
    time.sleep(5)

