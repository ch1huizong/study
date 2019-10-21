#! /usr/bin/env python3
# -*-coding:utf-8 -*-
# @Time    : 2019/06/16 20:17:48
# @Author  : che
# @Email   : ch1huizong@gmail.com
# 把一个进程转化为守护进程的方法
# 可以作为原型

import sys
import os
import time


def daemonize(stdin="/dev/null", stdout="/dev/null", stderr="/dev/null"):
    try:
        pid = os.fork()
        if pid > 0:
            sys.exit(0)
    except OSError as e:
        sys.stderr.write("fork #1 failed: (%d) %s\n"(e.errno, e.strerror))
        sys.exit(1)

    os.chdir("/")  # 修改子进程环境
    os.umask(0)
    os.setsid()

    try:  # 继承第一个fork和setsid的环境
        pid = os.fork()
        if pid > 0:
            sys.exit(0)
    except OSError as e:
        sys.stderr.write("fork #2 failed: (%d) %s\n"(e.errno, e.strerror))
        sys.exit(1)

    for f in [sys.stdout, sys.stderr]:
        f.flush()

    si = open(stdin, "r")
    so = open(stdout, "a+")
    se = open(stderr, "a+")
    os.dup2(si.fileno(), sys.stdin.fileno())  # 重置标准输入和输出
    os.dup2(so.fileno(), sys.stdout.fileno())
    os.dup2(se.fileno(), sys.stderr.fileno())


def mod_5_watcher():
    start_time = time.time()
    end_time = time.time() + 20
    while time.time() < end_time:
        now = time.time()
        if int(now) % 5 == 0:
            sys.stderr.write("Mod 5 at %s\n" % now)
        else:
            sys.stdout.write("No mod 5 at %s\n" % now)
        time.sleep(1)


if __name__ == "__main__":
    daemonize(stdout="/tmp/stdout.log", stderr="/tmp/stderr.log")
    mod_5_watcher()
