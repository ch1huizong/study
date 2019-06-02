#! /usr/bin/env python
# -*- coding:UTF-8 -*-

# 利用poll建立客户端, 操作系统提供的特性

import socket
import sys
import select

port = 51423
host = 'localhost'

spinsize = 10
spinpos = 0
spindir = 1

# 明白了！spinpos等于‘|' 索引处'
def spin():
    global spinsize, spinpos, spindir
    spinstr = '.' * spinpos + \
                '|' + '.'* (spinsize - spinpos -1)
    sys.stdout.write('\r' + spinstr + ' ')
    sys.stdout.flush()

    spinpos += spindir # next
    if spinpos < 0:
        spindir = 1
        spinpos = 1
    elif spinpos >= spinsize:
        spinpos -= 2
        spindir = -1

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))

#建立poll对象
p = select.poll()
p.register(s.fileno(), select.POLLIN | select.POLLERR | select.POLLHUP)
while True:
    results = p.poll(50)  # 1/20s
    if len(results):
        if results[0][1] == select.POLLIN:
            data = s.recv(4096)
            if not len(data):
                print("\rRemote end closed connection; exiting.")
                break
            sys.stdout.write("\rReceived: "+data)
            sys.stdout.flush()
        else:
            print "\rProblem occured; existing."
            sys.exit(0)

    spin()

