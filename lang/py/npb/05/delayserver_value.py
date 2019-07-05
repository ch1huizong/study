#! /usr/bin/env python
# -*- coding:UTF-8 -*-
# 每隔5秒向客户端发送信息 

import socket
import time
import traceback

host = ''
port = 51423

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind((host,port))
s.listen(1)
print "Waiting for connections..."

while True:
    try:
        clientsock, clientaddr = s.accept()
    except KeyboardInterrupt:
        raise
    except:
        traceback.print_exc()
    
    # 处理链接
    try:
        print "Got connection from ",clientsock.getpeername()
        while True:
            try:
                clientsock.sendall(time.ctime()+"\n")
            except:
                break
            time.sleep(5)
    except (KeyboardInterrupt, SystemExit):
        raise
    except:
        traceback.print_exc()

    # 关闭连接,除非发生错误
    try:
        clientsock.close()
    except KeyboardInterrupt:
        raise
    except:
        traceback.print_exc()


