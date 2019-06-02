#! /usr/bin/env python
# -*- coding:UTF-8 -*-
# 广播接收端

import socket
import traceback

host = ''
port = 51423

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1) # 支持处理广播数据
s.bind((host,port))

while True:
    try:
        message, address = s.recvfrom(8192)
        print "Got data from ",address
        s.sendto("Hi,I'm here!", address)
    except (KeyboardInterrupt, SystemExit):
        raise
    except:
        traceback.print_exc()
