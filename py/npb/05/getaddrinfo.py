#! /usr/bin/env python
# -*- coding:UTF-8 -*-
# 得到特定主机的ipv4和ipv6地址

import socket
import sys

host, port = sys.argv[1:]

results = socket.getaddrinfo(host,port,0,socket.SOCK_STREAM)

for result in results:
    print '-'*60
    if result[0] == socket.AF_INET:
        print "Family: AF_INET"
    elif result[0] == socket.AF_INET6:
        print "Family: AF_INET6"
    else:
        print "Family: ",result[0]

    if result[1] == socket.SOCK_STREAM:
        print "Sock Type: SOCK_STREAM"
    elif result[1] == socket.SOCK_DGRAM:
        print "Sock Type: SOCK_DGRAM"
    else:
        print "Sock Type: ",result[1]

    print "Protocol: ", result[2]
    print "Canonical Name:",result[3]
    print "Socket Address: ",result[4]


