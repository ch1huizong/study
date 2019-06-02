#! /usr/bin/env python 
# -*- coding:UTF-8
# UDP时间服务器,手写

import socket
import time
import struct
import traceback

host = ''
port = 51423

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind((host,port))

while True:
    try:
        message, address = s.recvfrom(8192)
        secs = int(time.time())  # from 1970,1,1 ..now
        secs -= 60*60*24
        secs += 2208988800       # from 1900,1,1... now
        reply = struct.pack("!I",secs)
        s.sendto(reply,address)
    except (KeyboardInterrupt, SystemExit):
        raise
    except:
        traceback.print_exc()



