#! /usr/bin/env python
# -*- coding:UTF-8

import socket
import sys

messages = [
        "This is the message.",
        "It will be sent",
        "in pairs."
        ]
server_address = ('localhost',10000)
socks = [ 
            socket.socket(socket.AF_INET,socket.SOCK_STREAM) ,
            socket.socket(socket.AF_INET,socket.SOCK_STREAM) ,
        ]

print >> sys.stderr, "connecting to %s port %s"% server_address
for sock in socks:
    sock.connect(server_address)

for msg in messages:
    for sock in socks:
        print >> sys.stderr, '%s: sending "%s" '%\
                (sock.getsockname(), msg)
        sock.send(msg)

    for sock in  socks:
        data = sock.recv(1024)
        print >> sys.stderr, '%s: received "%s"'%\
                (sock.getsockname(),data)
        if not data:
            print >> sys.stderr,"closing socket", sock.getsockname()
            sock.close()

