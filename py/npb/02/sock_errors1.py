#! /usr/bin/env python
# -*- coding: UTF-8
# 测试错误发生的不同条件
# 注意shutdown

import socket
import sys
import time

host = sys.argv[1]
textport = sys.argv[2]
filename = sys.argv[3]

try:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.error, e:
    print "Strange error creating socket: %s" % e
    sys.exit(1) 

try:
    port = int(textport)
except ValueError:
    try:
        port = socket.getservbyname(textport,'tcp')
    except socket.error, e:
        print "Couldn't find your port: %s" % e
        sys.exit(1)

try:
    s.connect((host,port))
except socket.gaierror,e:
    print "Address-related error connecting to server:%s" % e
    sys.exit(1)
except socket.error,e:
    print "Connection error:%s" % e
    sys.exit(1)

print "sleeping..."
time.sleep(10)
print "Continuing."


# 构造HTTP请求报文,为何总是不返回页面?
# 使用HTTP/1.0

try: 
    s.sendall("GET %s HTTP/1.0\r\n\r\n"% filename)
except socket.error,e:
    print "Error sending data: %s" % e
    sys.exit(1)

try:
    s.shutdown(1)  #关闭写端，确保服务端收到数据
except socket.error,e:
    print "Error sending data(detected by shutdown):%s" % e
    sys.exit(1)

while True:
    try:
        buf = s.recv(2048)
    except socket.error,e:
        print "Error receiving data: %s" % e
        sys.exit(1)
    if not len(buf):
        break
    sys.stdout.write(buf)
