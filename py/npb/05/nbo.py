#! /usr/bin/env python
# -*- coding:UTF-8 -*-
# 网络字节顺序

import struct
import sys

def pack16(num):
    return struct.pack('!H',num)

def pack32(num):
    return struct.pack('!I',num)

def unpack16(data):
    return struct.unpack('!H',data)[0]

def unpack32(data):
    return struct.unpack('!I',data)[0]

def sendstring(data):
    return pack32(len(data)) + data

print "Enter a string:"
str = sys.stdin.readline().rstrip()

print repr(sendstring(str))
