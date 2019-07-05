#! /usr/bin/env python
# -*- coding:UTF-8 -*-

import socket
import sys
import select

port = 51423
host = 'localhost'

spinsize = 10
spinpos = 0
spindir = 1

def spin():
    global spinsize, spinpos, spindir
    spinstr = '.' * spinpos + \
                '|' + '.'* (spinsize - spinpos -1)
    sys.stdout.write('\r' + spinstr + ' ')
    sys.stdout.flush()

    spinpos += spindir
    if spinpos < 0:
        spindir = 1
        spinpos = 1
    elif spinpos >= spinsize:
        spinpos -= 2
        spindir = -1

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))

while True:
    infds, outfds, errfds = select.select([s],[],[s],0.05)
    if len(infds):
        data = s.recv(4096)
        if not len(data):
            print("\rRemote end closed connection; exiting.")
            break
        sys.stdout.write("\rReceived: "+data)
        sys.stdout.flush()
    if len(errfds):
        print "\rProblem occured; existing."
        sys.exit(0)
    spin()

