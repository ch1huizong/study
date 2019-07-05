#! /usr/bin/env python
# -*- coding:UTF-8 -*-
# 使用forking 技术的echoserver
# last-modified: sys.exit缩进

import socket
import os
import traceback
import sys

def reap():
    while True:
        try:
            result = os.waitpid(-1,os.WNOHANG)
            if not result[0]: # 测试PID是否是0,为什么？
                break
        except:
            break
        print "Reaped Child process %d" % result[0]

host = ''
port = 51423

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind((host,port))
s.listen(1)

while True:
    try:
        clientsock, clientaddr = s.accept()
    except KeyboardInterrupt:
        raise
    except:
        traceback.print_exc()
        continue

    reap()  #清除上一次的子僵尸进程,是否有多个的可能行？
    
    try:
        pid = os.fork()
    except:
        print "Bad THING HAPPENED:fork failed."
        clientsock.close()
        continue

    if pid:
        clientsock.close()  # 父进程中，关闭clientsock,只剩server sock(s)
        continue
    else:
        s.close()  # 子进程中，关闭serversock,只剩client sock

        try:
            print "Child from %s being handled by PID %d"%\
                    (clientsock.getpeername(),os.getpid())

            while True:
                data = clientsock.recv(4096)
                if not len(data):
                    break
                clientsock.sendall(data)
        except (KeyboardInterrupt,SystemExit):
            raise
        except:
            traceback.print_exc()

        # 关闭连接
        try:
            clientsock.close()
        except KeyboardInterrupt:
            raise
        except:
            traceback.print_exc()
            
        #必须有！
        sys.exit(0)

