#!/usr/bin/env python3
# -*- coding:UTF-8
from multiprocessing.connection import Client

conn = Client(('45.77.93.132', 15000), authkey=b'12345')

conn.send((3, 5))
r = conn.recv()
print(r)

conn.send(("hello", "world"))
r = conn.recv()
print(r)

conn.close()
