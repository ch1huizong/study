#! /usr/bin/env python
# -*- coding:UTF-8 -*-
# 使用Unix域套接字来进行进程间通信

import socket
import sys
import os

server_address = '/tmp/uds_socket'

try:
    os.unlink(server_address)
except OSError:
    if os.path.exists(server_address):
        raise

sock = socket.socket(socket.AF_UNIX,type=socket.SOCK_STREAM)

print >>sys.stderr, 'Starting up on %s'% server_address
sock.bind(server_address)
sock.listen(1)

while True:
    print >> sys.stderr,"Waiting for a connection..."
    connection, client_address = sock.accept()
    try:
        print >> sys.stderr,"Connection from ",client_address
        while True:
            data = connection.recv(16)
            print >> sys.stderr, "received %s" %data
            if data:
                print >> sys.stderr, "sending data back to the client"
                connection.sendall(data)
            else:
                print >> sys.stderr, "no data from" ,client_address
                break
    finally:
        connection.close()
        
