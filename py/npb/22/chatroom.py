#! /usr/bin/env python
# -*- coding:UTF-8 -*-
# 使用poll的chat server

import socket,traceback, os, sys, select

class stateclass(object):
    stdmask = select.POLLERR | select.POLLHUP | select.POLLNVAL

    def __init__(self, mastersock): # 关键是状态
        self.p = select.poll()
        self.mastersock = mastersock # 主监控套接字
        self.watchread(mastersock)
        self.readbuffers = {}    # 每一个socket的读入数据 
        self.writebuffers = {}   # 每一个socket的待发送数据
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
        self.writebuffers[fd] = "Welcome to the chat server, %s\n" % str(sock.getpeername())
        self.readbuffers[fd] = ""
        self.sockets[fd] = sock

    def sendtoall(self, text, originfd):
        for line in text.split('\n'):   # 自己处理换行
            line = line.strip()
            transmittext = str(self.fd2socket(originfd).getpeername()) + \
                ":" + line + "\n"
            for fd in self.writebuffers.keys():
                self.writebuffers[fd] += transmittext
                self.watchboth(fd)

    # 事件处理
    def readevent(self, fd):
        try:
            self.readbuffers[fd] += self.fd2socket(fd).recv(4096)
        except:
            self.closeout(fd)
        self.watchboth(fd)   # 可以忽略吗？no ba

        parts = self.readbuffers[fd].split('SEND')
        if len(parts) < 2: # 接受的内容没有send,返回
            return
        elif parts[-1] == '':
            self.readbuffers[fd] = "" # 清空
            sendlist = parts[:-1]
        else:
            self.readbuffers[fd] = parts[-1]  # 余下未以send结尾部分，下次数据接收时再处理
            sendlist = parts[:-1]
        for item in sendlist:
            self.sendtoall(item.strip(),fd)

    
    def writeevent(self, fd):
        if not len(self.writebuffers[fd]):
            self.watchread(fd)  # 没数据了，改设置为只读
            return
        try:
            byteswritten = self.fd2socket(fd).send(self.writebuffers[fd])
        except:
            self.closeout(fd)
        self.writebuffers[fd] = self.writebuffers[fd][byteswritten:]

        if not len(self.writebuffers[fd]): # 发送完数据了?
            self.watchread(fd)  # 设置为只读

    def errorevent(self, fd):
        self.closeout(fd)

    def closeout(self, fd):
        self.dontwatch(fd)
        try:
            self.fd2socket[fd].close()
        except:
            pass

        del self.writebuffers[fd]
        del self.sockets[fd]

    # 主循环
    def loop(self):
        while True:
            result = self.p.poll() 
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

