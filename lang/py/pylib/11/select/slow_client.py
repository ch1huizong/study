#! /usr/bin/env python
# -*- coding:UTF-8

import socket
import sys
import time

server_address = ('localhost',10000)
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print >> sys.stderr, "connecting to %s port %s"% server_address

s.connect(server_address)
time.sleep(1)

messages = [
        "Part one of the message",
        "Part two of the message",
        ]

expected_amount = len(''.join(messages))

try:
    #send
    for msg in messages:
        print >> sys.stderr, "sending '%s' "%msg
        s.sendall(msg)
        time.sleep(1.5)
    

    # receive
    amout_received = 0
    while amout_received < expected_amount:
        data = s.recv(16)
        amout_received += 16
        print >> sys.stderr, "received '%s'"%data
        
finally:
    print >> sys.stderr, "closing socket"
    s.close()

