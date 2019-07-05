#! /usr/bin/env python
# -*- coding:UTF -*-
# 僵尸进程，没一个进程结束时的必经状态.
# 子进程结束时，若父进程没有进行处理或设置显示忽略，
# 则子进程变成僵尸进程;当父进程也结束时，子进程会被
# init接管清除。
#
# 用途：因为父进程会使用到子进程结束时的一些信息，所以
# 系统设计的时候会有僵尸进程的概念。

import os
import time

print "Before the fork, my PID is" ,os.getpid()

pid = os.fork()

if pid:  # 父进程未结束，子进程一直保持僵尸状态;结束时，僵尸进程才被init清理
    print "Hello from the parent. The child will be PID %d"%pid
    print "Sleeeping 120 second..."
    time.sleep(120)

