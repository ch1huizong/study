#!/usr/bin/env python
# -*- coding:UTF-8
# 客户端
from multiprocessing.connection import Client
conn = Client(('192.168.0.149',15000),authkey='12345')

conn.send((3,5))
r = conn.recv()
print r

conn.send(("hello","world"))
r = conn.recv()
print r

conn.close()
