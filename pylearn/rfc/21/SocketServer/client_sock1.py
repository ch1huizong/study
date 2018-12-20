#! /usr/bin/env python
# -*- coding:UTF-8 -*-

import socket
import sys
import time

HOST, PORT = "localhost",9999
data = "".join(sys.argv[1:])

#sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)   #udp


#try:
#    sock.connect((HOST,PORT))
#    sock.sendall(data + "\n")
#
#    received = sock.recv(1024)
#finally:
#    sock.close()

for i in range(100):
    sock.sendto(data + "\n", (HOST,PORT))
    received = sock.recv(1024)
    print "Sent:    {}".format(data)
    print "Received: {}".format(received)
    time.sleep(10000)

