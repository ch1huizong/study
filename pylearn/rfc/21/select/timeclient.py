#!/usr/bin/env python
# -*- coding:UTF-8 -*-

from socket import *
from threading import Thread

def gettime(address):
    sock = socket(AF_INET,SOCK_STREAM)
    sock.connect(address)
    tm = sock.recv(1024)
    sock.close()
    print("The time is %s" % tm.decode('ascii'))

t1 = [ Thread(target=gettime, args=(('localhost',10000),)) for i in range(100) ]
t2 = [ Thread(target=gettime, args=(('localhost',11000),)) for i in range(100) ]
for a,b in map(None,t1,t2):
    a.run()
    b.run()
    
