#! /usr/bin/env python
# -*- coding:UTF-8 -*-
# 使用poll的echo server

import socket,traceback, os, sys, select

class stateclass(object):
    stdmask = select.POLLERR | select.POLLHUP | select.POLLNVAL

    def __init__(self, mastersock): # 关键是状态
        self.p = select.poll()
        self.mastersock = mastersock # 主监控套接字
        self.watchread(mastersock)
        self.buffers = {} # 每一个链接的待发送消息,缓存
        self.sockets = { mastersock.fileno():mastersock } # 每一链接

    # 帮助函数
    def fd2socket(self, fd):
        return self.sockets[fd]

    def watchread(self, fd):
        self.p.register(fd, select.POLLIN | self.stdmask)

    def watchwrite(self, fd):
        self.p.register(fd, select.POLLOUT | self.stdmask)
    
    def watchboth(self, fd):
        self.p.register(fd, select.POLLIN| select.POLLOUT | self.stdmask)

    def dontwatch(self, fd):
        self.p.unregister(fd)

    def newconn(self, sock):
        fd = sock.fileno()
        self.watchboth(fd)
        
        # 待发送消息
        self.buffers[fd] = "Welcome to the echoserver, %s\n" % str(sock.getpeername())
        self.sockets[fd] = sock

    # 事件处理
    def readevent(self, fd):
        try:
            self.buffers[fd] += self.fd2socket(fd).recv(4096)
        except:
            self.closeout(fd)
        self.watchboth(fd)   # 可以忽略吗？no ba
    
    def writeevent(self, fd):
        if not len(self.buffers[fd]):
            self.watchread(fd)  # 没数据了，改设置为只读
            return
        try:
            byteswritten = self.fd2socket(fd).send(self.buffers[fd])
        except:
            self.closeout(fd)
        self.buffers[fd] = self.buffers[fd][byteswritten:]

        if not len(self.buffers[fd]): # 发送完数据了?
            self.watchread(fd)  # 设置为只读

    def errorevent(self, fd):
        self.closeout(fd)

    def closeout(self, fd):
        self.dontwatch(fd)
        try:
            self.fd2socket[fd].close()
        except:
            pass

        del self.buffers[fd]
        del self.sockets[fd]

    # 主循环
    def loop(self):
        while True:
            result = self.p.poll() # 可读则读（触发？),可写则写？
            for fd, event in result:
                if fd == self.mastersock.fileno() and event == select.POLLIN: # 主关键字的读事件
                    try:
                        newsock, addr = self.fd2socket(fd).accept()
                        newsock.setblocking(0)
                        print "Got connection from", newsock.getpeername()
                        self.newconn(newsock)
                    except:
                        pass
                elif event == select.POLLIN:
                    self.readevent(fd)
                elif event == select.POLLOUT:
                    self.writeevent(fd)   # 第二次poll才写
                else:
                    self.errorevent(fd)


host = ''
port = 51423

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(1)
s.setblocking(0)

state = stateclass(s)
state.loop()

