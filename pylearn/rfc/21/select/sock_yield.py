#! /usr/bin/env python
# -*- coding:UTF-8 -*-
# socket的没一个操作变成了协程
# 会实现一定形式的并发？

from ioloop import *
import time

class CoSocket(object):
    def __init__(self, sock):
        self.sock = sock

    def close(self):
        yield self.sock.close()

    def bind(self, addr):
        yield self.sock.bind(addr)

    def listen(self, backlog):
        yield self.sock.listen(backlog)

    def connect(self, addr):
        yield WriteWait(self.sock)
        yield self.sock.connect(addr)

    def accept(self):
        yield ReadWait(self.sock)
        conn, addr = self.sock.accept()
        yield CoSocket(conn), addr

    def send(self, bytes):
        while bytes:
            evt = yield WriteWait(self.sock)
            nsent = self.sock.send(bytes)
            bytes = bytes[nsent:]
   
    def recv(self,maxsize):
        yield ReadWait(self.sock)
        yield self.sock.recv(maxsize)

if __name__ == '__main__':

    from socket import socket, AF_INET, SOCK_STREAM
    import time
    def timeserver(address):
        s = CoSocket(socket(AF_INET,SOCK_STREAM))
        yield s.bind(address)
        yield s.listen(5)
        while True:
            conn, addr = yield s.accept()
            print conn
            print "Connection from %s" % str(addr)
            resp = time.ctime() + "\r\n"
            yield conn.send(resp.encode('ascii'))
            yield conn.close()

    sched = Scheduler()
    sched.new(timeserver(('',10000)))
    sched.new(timeserver(('',11000)))
    sched.mainloop()
