#! /usr/bin/env python
# -*- coding:UTF-8 -*-
# 绑定到特殊地址 

import socket
import traceback

host = '127.0.0.1'
port = 51423

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind((host,port))
s.listen(1)

while True:
        clientsock, clientaddr = s.accept()

        print "Got connection from ", clientsock.getpeername()

        while True:
            data = clientsock.recv(4096)
            if not len(data):
                break
            clientsock.sendall(data)

        clientsock.close()
