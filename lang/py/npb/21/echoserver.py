#! /usr/bin/env python
# -*- coding:UTF-8 -*-
# 使用多线程技术的echoserver

import socket
import os
import sys
import traceback
import threading

host = ''
port = 51423

def handlechild(clientsock): 
    print "New child",threading.currentThread().getName()
    print "Got connection from", clientsock.getpeername()
    while True:
        data = clientsock.recv(4096)
        if not len(data):
            break
        clientsock.sendall(data)
    clientsock.close()

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
s.bind((host,port))
s.listen(1)

while True:
    try:
        clientsock, clientaddr = s.accept() # 线程技术，可以保证主线程是接收unix信号的唯一代码
    except KeyboardInterrupt:
        raise
    except:
        traceback.print_exc()
        continue

    t = threading.Thread(target = handlechild, args=[clientsock,])
    t.setDaemon(True)
    t.start()

