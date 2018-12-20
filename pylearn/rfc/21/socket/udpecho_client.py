#! /usr/bin/env python
# -*- coding:UTF-8 -*-

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(b'Hello World',("", 10000))
resp, addr = s.recvfrom(256)
print resp

s.sendto(b'Spam',("", 10000))
resp, addr = s.recvfrom(256)
print resp

import itertools
for item in itertools.repeat("Hello World"):
    s.sendto(item,("", 10000))
    resp, addr = s.recvfrom(256)
    print resp

s.close()

