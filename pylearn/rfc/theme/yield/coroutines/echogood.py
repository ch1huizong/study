#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# echogood.py
#
# A another attempt at an echo server.  This one works because
# of the I/O waiting operations that suspend the tasks when there
# is no data available.  Compare to echobad.py

from socket import *
from pyos7 import *


def handle_client(client,addr):  # client task
    print "Connection from", addr
    while True:
        yield ReadWait(client)
        data = client.recv(65536)
        if not data:
            break
        yield WriteWait(client)
        client.send(data)
    client.close()
    print "Client closed"


def server(port):     # server task
    print "Server starting"
    sock = socket(AF_INET,SOCK_STREAM)
    sock.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    sock.bind(("",port))
    sock.listen(5)
    while True:
        yield ReadWait(sock)
        client,addr = sock.accept()  # 前面已经判断了，不阻塞了立马返回
        yield NewTask(handle_client(client,addr))    


def alive():  # alive task
    while True:
        print "I'm alive!"
        yield

# server task的激活是靠iotask, 靠select监控的fd准备好
# iotask的不停运行，会移进/移出client_sock/server_sock的任务
sched = Scheduler()
sched.new(alive())
sched.new(server(45000))
sched.mainloop()  # 内部有一iotask
