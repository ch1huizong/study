#! /usr/bin/env python
# -*- coding:UTF-8 -*-
# UDP应答服务器

import socket
import traceback

host = ''
port = 51423

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # 只用了一个socket
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind((host,port))

while True:
    try:
        message, address = s.recvfrom(8192)
        print "Got data from ",address
        s.sendto(message, address)
    except (KeyboardInterrupt, SystemExit):
        raise
    except:
        traceback.print_exc()
