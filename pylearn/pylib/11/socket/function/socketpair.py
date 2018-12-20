#! /usr/bin/env python
# -*- coding:UTF-8

import socket
import os

parent, child = socket.socketpair()

pid = os.fork()

if pid:
    print "In parent, sending message"
    child.close()
    parent.sendall('ping')

    response = parent.recv(1024)
    print "response from child:",response
    parent.close()
else:
    print "In child, waiting for message"
    parent.close()
    message = child.recv(1024)
    print "Message from parent:",message
    child.sendall('Pong')
    child.close()
