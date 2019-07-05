#!/usr/bin/env python
# -*- coding:UTF-8 -*-

from socket import *

s = socket(AF_INET,SOCK_STREAM)
s.connect(('localhost',9999))
tm = s.recv(1024)
s.close()
print("The time is %s" % tm.decode('ascii'))
