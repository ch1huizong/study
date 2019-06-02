#! /usr/bin/env python
# -*- coding:UTF-8 -*-
# 利用线程池的技术,需要跟踪线程的运行状态
# 需要好好研究研究

import socket
import threading
import os
import sys
import time
import traceback

host = ''
port = 51423
MAXTHREADS = 3

lockpool = threading.Lock()
# 以下两个变量跟踪线程的运行状态
busylist = {}       #线程运行列表,与下互斥
waitinglist = {}    #线程等待列表
queue = []          #存放待处理的客户端连接

sem = threading.Semaphore(0) # 线程会等待sem

def handleconnection(clientsock): # 此函数在主控中
    lockpool.acquire() # queue也需要锁定 
    print "Received new client connection."
    try:
        # 达到最大工作线程数量了
        if len(waitinglist) == 0 and (threading.active_count()-1)>= MAXTHREADS:
            clientsock.close()
            return
        # 开始时，建立线程或者未达到最大数量
        if len(waitinglist) == 0: 
            startthread()

        queue.append(clientsock)
        sem.release() # 通知线程有conn到达
    finally:
        lockpool.release()

def startthread():
    print "Staring new client processor thread"
    t = threading.Thread(target = threadworker)
    t.setDaemon(1)
    t.start()

def threadworker():
    global waitinglist, lockpool, busylist  # 子线程引用全局数据
    time.sleep(1)   # 模拟线程初始化
    name = threading.currentThread().getName()
    
    try:
        lockpool.acquire() # 初始化数据结构
        try:
            waitinglist[name] = 1
        finally:
            lockpool.release()

        processclients()  # waiting...
    finally:
        if name in waitinglist:
            del waitinglist[name]
        if name in busylist:
            del busylist[name]

        startthread()

def processclients():
    global sem, queue, waitinglist, busylist, lockpool

    name = threading.currentThread().getName()
    while True:
        sem.acquire()  # 获取数据（链接）,等待的会阻塞在这
        lockpool.acquire()

        try:
            clientsock = queue.pop(0)
            del waitinglist[name] 
            busylist[name] = 1  # 设置为running
        finally:
            lockpool.release()

        try:
            print "[%s] Got connection from %s"%\
                    (name, clientsock.getpeername())
            clientsock.sendall("Greetings. You are being serviced by %s.\n"%name)
            while True:
                data = clientsock.recv(4096)
                if data.startswith("DIE"):
                    sys.exit(0)
                if not data:
                    break
                clientsock.sendall(data)
        except (KeyboardInterrupt,SystemExit):
            raise
        except:
            traceback.print_exc()

        try:
            clientsock.close()
        except (KeyboardInterrupt,SystemExit):
            raise
        except:
            traceback.print_exc()

        # 处理完数据，更新数据结构 
        lockpool.acquire()
        try:
            del busylist[name] 
            waitinglist[name] = 1
        finally:
            lockpool.release()


def listener():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
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
        
        handleconnection(clientsock)

listener()
