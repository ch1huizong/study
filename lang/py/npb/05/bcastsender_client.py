#! /usr/bin/env python
# -*- coding: UTF-8
# 广播发送端 

import socket
import sys

dest = ('<broadcast>', 51423)

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)
s.sendto("Hello",dest)

print "Looking for replies; press Ctrl-C to stop."
while True:
    (buf,address) = s.recvfrom(2048)
    if not len(buf):
        break
    print "Received from %s: %s" % (address,buf)
