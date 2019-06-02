#! /usr/bin/env python
# -*- coding:UTF-8 -*-

import socket

host = ''
port = 51423

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind((host,port))
s.listen(5)

print "Server is running on port %d; please Ctrl-C to terminate." % port

while True:
    clientsock, clientaddr = s.accept()
    print "Connection from %s."%str(clientaddr)
    clientfile = clientsock.makefile('rw',0)
    clientfile.write("Welcome, " + str(clientaddr)+"\r\n")
    clientfile.write("Please enter a string: ")
    line = clientfile.readline().strip()
    clientfile.write("You entered %d characters.\n" % len(line))
    clientfile.close() # 服务器主动关闭
    clientsock.close()
