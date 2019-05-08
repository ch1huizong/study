#! /usr/bin/env python
# -*- coding:UTF-8 -*-
# 使用线程，添加网络监视服务功能，集合到应用程序中

# 基本任务
bottles = 10000000

def drink_beer():  # 代表CPU形任务，占用资源
    remaining = 12.0
    while remaining > 0.0:
        remaining -= 0.1

def drink_bottles(): # 模拟主循环
    global bottles
    while bottles > 0:
        drink_beer()
        bottles -= 1

import socket
import threading
def server(port):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind(('',port))
    s.listen(5)
    while True:
        client, addr = s.accept()
        client.send(("%d bottles\r\n" % bottles).encode("ascii"))
        client.close()

s = threading.Thread(target=server,args=(10000,)) # 代表一个监控服务线程
s.daemon = True
s.start()
drink_bottles()
