#! /usr/bin/env  python
# -*- coding:UTF-8 -*-
# TCP简单客户端

import socket

print "Creating socket..."
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print "done."

print "Connecting to remote host..."
s.connect(("121.42.159.81",51423))
print "done."
