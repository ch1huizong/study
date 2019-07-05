#! /usr/bin/env python
# -*- coding:UTF-8 -*-
# 基于select的回显服务器

import select
import socket
import sys

HOST = 'localhost'
PORT = 10000
BUFFER_SIZE = 1024

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)

inputs = [ server, sys.stdin ]
running = True

while running:
    try:
        readable, writeable, exceptional = select.select(inputs, [], [])
    except select.error:
        break

    for sock in readable:
        if sock == server:
            conn, addr = server.accept()
            inputs.append(conn)
        elif sock == sys.stdin:
            junk = sys.stdin.readlines()
            running = False
        else:
            try:
                data = sock.recv(BUFFER_SIZE)
                if data:
                    sock.send(data) 
                    if data.endswith("\r\n\r\n"):
                        inputs.remove(sock)
                        sock.close()
                else:
                    inputs.remove(sock)
                    sock.close()
            except socket.error:
                inputs.remove(sock)

server.close()


