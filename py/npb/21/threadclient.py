#! /usr/bin/env python
# -*- coding:UTF -*-
# 使用条件变量，获得队列并等待队列上有数据
# 使用条件变量有点复杂吧?

import socket
import sys
import time
from threading import Condition, Thread

host = sys.argv[1]
textport = sys.argv[2]
filename = sys.argv[3]
cv = Condition()
spinners = '|/-\\'
spinpos = 0
equeue = []

def fwrite(buf):
    sys.stdout.write(buf)
    sys.stdout.flush()

def spin():  
    global spinpos
    fwrite(spinners[spinpos] + '\b')
    spinpos += 1
    if spinpos >= len(spinners):
        spinpos = 0

def uithread():                 # 消费者线程, 主要是播放动画
    while True:
        cv.acquire()            # 获得队列是一个问题
        while not len(equeue):  # 队列上有数据是另一个问题
            cv.wait(0.15)       # 等待并释放锁定0.15s返回重新获得锁，保证安全访问序列
            spin()              # 若此期间生产者获得了cv,则一直wait吗？ 好像是？
        
        msg = equeue.pop(0)
        cv.release()
        if msg == 'QUIT':
            fwrite("\n")
            sys.exit(0)
        fwrite(" \n %s\r" % msg)

def msg(message):               # 生产者线程
    cv.acquire()
    equeue.append(message)
    cv.notify()
    cv.release()

t = Thread(target = uithread)
t.setDaemon(1)
t.start()

try:
    msg("Creating socket object")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, e:
    print "Strang error creating socket: %s" % e
    sys.exit(1)

try:
    port = int(textport)
except ValueError:
    try:
        port = socket.getservbyname(textport, 'tcp')
    except socket.error, e:
        print "Couldn't find your port: %" % e
        sys.exit(1)

msg('Connecting to %s:%d' % (host, port))
time.sleep(5)
try:
    s.connect((host, port))
except socket.gaierror, e:
    print "Address-related error connecting to server: %" % e
    sys.exit(1)
except socket.error,e:
    print "Connection error: %s" % e
    sys.exit(1)

msg('Sending query')
time.sleep(5)
try:
    s.sendall('GET %s HTTP/1.0\r\n\r\n' % filename)
except socket.error, e:
    print "Error sending data %s" % e
    sys.exit(1)

msg("Shutting down socket")
time.sleep(2)
try:
    s.shutdown(1)
except socket.error, e:
    print "Error sending data(detected by shutdown) %s" % e
    sys.exit(1)

msg('Receiving data')
count  = 0
while True:
    try:
        buf = s.recv(2048)
    except socket.error, e:
        print "Error receiving data:%s" % e
        sys.exit(1)
    if not len(buf):
        break
    count += len(buf)

msg("Received %d bytes" % count)
msg("QUIT")
t.join()
