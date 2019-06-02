#! /usr/bin/env python
# -*- coding:UTF-8 -*-
# TCP基本服务器

import socket
import time

host = ''
port = 51423

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind((host,port))
print "Waiting for connections..."
s.listen(1)

while True:
    clientsock, clientaddr = s.accept()
    # 处理客户端请求
    print "Got connection from ",clientsock.getpeername()
    time.sleep(100)
    clientsock.close()


