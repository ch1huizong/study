#! /usr/bin/env python
# -*- coding:UTF-8 -*-
# 使用forking 技术,多网络链接访问同一文件
# lastaccess.txt将被重写
# 最后修改：sys.exit(0)缩进了

# 问题：
#    共享锁是不是唯一的lock的在读进程之间切换实现的?

import socket
import os
import traceback
import sys
import time
import fcntl

def getlastaccess(fd,ip):   #读
    fcntl.flock(fd,fcntl.LOCK_SH)
    try:
        fd.seek(0)
        for line in fd.readlines():
            fileip, accesstime = line.strip().split('|')
            if fileip == ip :
                return accesstime
        return None
    finally:
        # 只有所有持有共享锁的进程释放后，才可以有进程持有独占锁
        fcntl.flock(fd, fcntl.LOCK_UN) 

# 在一个进程持有独占锁的时候，其它所有进程都不能持有锁（共享锁和独占锁）
def writelastaccess(fd,ip): #写
    fcntl.flock(fd,fcntl.LOCK_EX)
    records = [] 
    try:
        fd.seek(0)
        for line in fd.readlines():
            fileip, accesstime = line.strip().split("|")
            if fileip != ip:
                records.append((fileip,accesstime))
        fd.seek(0)
        for fileip, accesstime in records + [ (ip,time.asctime()) ]:
            fd.write("%s|%s\n"%(fileip,accesstime))
            fd.truncate()
    finally:
        fcntl.flock(fd, fcntl.LOCK_UN)


def reap():
    while True:
        try:
            result = os.waitpid(-1,os.WNOHANG)
            if not result[0]:
                break
        except:
            break
        print "Reaped Child process %d"%result[0]

host = ''
port = 51423

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind((host,port))
s.listen(1)
fd = open("lastaccess.txt","w+")

while True:
    try:
        clientsock, clientaddr = s.accept()
    except KeyboardInterrupt:
        raise
    except:
        traceback.print_exc()
        continue

    reap()  #清除上一次的子僵尸进程

    try:
        pid = os.fork() # 不能fork
    except:
        print "Bad THING HAPPENED:fork failed." 
        clientsock.close() # 关闭，并且不应该向clientsock写数据,防止主控长时间阻塞
        continue

    if pid:
        clientsock.close()  # 父进程中，关闭clientsock,只剩server sock(s)
        continue
    else:
        s.close()  # 子进程中，关闭serversock,只剩client sock

        try:
            print "Child from %s being handled by PID %d"%\
                    (clientsock.getpeername(),os.getpid())

            ip = clientsock.getpeername()[0]
            clientsock.sendall("Welcome, %s.\n" % ip)
            last = getlastaccess(fd,ip) 
            
            if last:
                clientsock.sendall("I last saw you at %s.\n" % last)
            else:
                clientsock.sendall("I never seen you before.\n")

            writelastaccess(fd,ip)
            clientsock.sendall("I have noted your connection at %s.\n"%\
                        getlastaccess(fd,ip))
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
            
    ####必须有！
    sys.exit(0)

