#! /usr/bin/env python
# -*- coding:UTF-8 -*-

import binascii
import socket
import struct
import sys

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address = ('localhost',10000)
sock.connect(server_address)

values = (1, 'ab', 2.7)
packer = struct.Struct('I 2s f')
packed_data = packer.pack(*values)

print 'values =',values

try:
    print >> sys.stderr,"sending %r"% binascii.hexlify(packed_data)
    sock.sendall(packed_data)
finally:
    print >> sys.stderr,"closing socket"
    sock.close()


