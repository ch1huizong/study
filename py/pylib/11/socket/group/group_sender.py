#! /usr/bin/env python
# -*- coding:UTF-8 -*-
# 组播发送者

import socket
import struct
import sys

message = 'very important message'
multicast_group = ('224.3.29.71',10000)

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.settimeout(0.2)        # 超时，防止无限等待
ttl = struct.pack('b',1)    
sock.setsockopt(socket.IPPROTO_IP,socket.IP_MULTICAST_TTL,ttl)  #生存期

try:
    print >> sys.stderr,"sending %s" % message
    sent = sock.sendto(message, multicast_group)

    while True:
        print >> sys.stderr,"waiting to receive"
        try:
            data, server = sock.recvfrom(16)
        except socket.timeout:
            print >> sys.stderr,"timed out, no more response"
            break
        else:
            print >> sys.stderr, "received %s from %s"%(data,server)
finally:
    print >> sys.stderr,"closing socket"
    sock.close()




