#! /usr/bin/env python
# -*- coding:UTF-8 -*-

import binascii
import socket
import struct
import sys

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address = ('localhost',10000)
sock.bind(server_address)
sock.listen(1)

unpacker = struct.Struct('I 2s f')

while True:
	print >>sys.stderr,"\nwaiting for a connection..."
	con, client_addr = sock.accept()
	try:
		data = con.recv(unpacker.size)
		print >> sys.stderr,"received %r" % binascii.hexlify(data)
		unpacked_data = unpacker.unpack(data)
		print >> sys.stderr,"unpacked:",unpacked_data
	finally:
		con.close()

