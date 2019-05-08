#! /usr/bin/env python
# -*- coding:UTF-8 -*-
# 在业务代码中嵌入轮循操作,集合到应用程序中,添加网络监视服务功能，

# 基本任务
bottles = 10000000

def drink_beer():  
    remaining = 12.0
    while remaining > 0.0:
        remaining -= 0.1

def drink_bottles():
    global bottles
    while bottles > 0:
        drink_beer()
        bottles -= 1
        sched.mainloop(count=1, timeout=0)  # 查询连接


import socket
from ioloop import *
from sock_yield import *

def server(port):
    s = CoSocket(socket.socket(socket.AF_INET,socket.SOCK_STREAM))
    yield s.bind(('',port))
    yield s.listen(5)
    while True:
        client, addr = yield s.accept()
        yield client.send(("%d bottles\r\n" % bottles).encode("ascii"))
        yield client.close()

sched = Scheduler()
sched.new(server(10000))
drink_bottles()

