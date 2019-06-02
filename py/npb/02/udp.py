#! /usr/bin/env python
# -*- coding: UTF-8
# udp客户端

import socket
import sys

host = sys.argv[1]
textport = sys.argv[2]

try:
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
except socket.error, e:
    print "Strange error creating socket: %s" % e
    sys.exit(1) 

try:
    port = int(textport)
except ValueError:
    try:
        port = socket.getservbyname(textport,'udp')
    except socket.error, e:
        print "Couldn't find your port: %s" % e
        sys.exit(1)

s.connect((host,port))  # 可以忽略
print "Enter data to transmit: "
data = sys.stdin.readline().strip()
s.sendall(data)
print "Looking for replies; press CTRl-C or CTRL-Break to stop."

while True:
    buf = s.recv(2048)  # 可能永远收不到数据，会阻塞;但tcp也会阻塞啊？
    if not len(buf):
        break
    sys.stdout.write(buf)
