#! /usr/bin/env python
# -*- coding:UTF-8 -*-
# 服务器错误测试

import socket
import traceback

host = ''
port = 51423

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind((host,port))
print "Waiting for connections..."
s.listen(1)

while True:
    try:                                        # first
        clientsock, clientaddr = s.accept()
    except KeyboardInterrupt:
        raise
    except:
        traceback.print_exc()
        continue
    
    try:                                        # two
        print "Got connection from ",clientsock.getpeername()
        # 连接处理代码
        # ...
    except (KeyboardInterrupt, SystemExit):
        raise
    except:
        traceback.print_exc()

    try:                                        # three
        clientsock.close()
    except KeyboardInterrupt:
        raise
    except:
        traceback.print_exc()
