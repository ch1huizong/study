#! /usr/bin/env python
# -*- coding:UTF-8 -*-

import socket
import sys

sock = socket.socket(socket.AF_UNIX,socket.SOCK_STREAM)
server_address = '/tmp/uds_socket'

print >>sys.stderr,'Connecting to %s'% server_address
try:
    sock.connect(server_address)
except socket.error,msg:
    print >> sys.stderr,msg
    sys.exit(1)

#发送数据
try:
    msg = "This is the message. It will be repeated."
    print >>sys.stderr,'Sending %s'%msg
    sock.sendall(msg)

    amount_received = 0
    amount_expected = len(msg)

    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += 16
        print >> sys.stderr,"received %s"%data
finally:
    print >> sys.stderr,"closing socket."
    sock.close()
    

