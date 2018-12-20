#! /usr/bin/env python
# -*- coding:UTF-8 -*-

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('',10000))
while True:
    data, address = s.recvfrom(256)
    print "Received a connection from %s" % str(address)
    s.sendto(b"echo:" + data, address)


