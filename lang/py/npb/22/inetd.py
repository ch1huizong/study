#! /usr/bin/env python
# -*- coding:UTF-8 -*-
# 异步守候进程服务器，监听多个socket端口,poll-forking实现

import socket, traceback, os, sys,select

class stateclass(object):
    def __init__(self):
        self.p = select.poll()
        self.mastersocks = {}   # 监听套接子
        self.commands = {}

    def fd2socket(self,fd):
        return self.mastersocks[fd]

    def addmastersock(self, sockobj, command):
        self.mastersocks[sockobj.fileno()] = sockobj
        self.commands[sockobj.fileno()] = command
        self.watchread(sockobj)

    def watchread(self, fd):
        self.p.register(fd, select.POLLIN)

    def dontwatch(self, fd):
        self.p.unregister(fd)

    def newconn(self, newsock, command):
        try:
            pid = os.fork()
        except:
            try:
                newsock.close()
            except:
                pass
            return
        
        if pid: # 父进程返回
            newsock.close()
            return

        for sock in self.mastersocks.values(): # 子进程处理
            sock.close()

        fd = newsock.fileno()
        os.dup2(fd, 0)
        os.dup2(fd, 1)
        os.dup2(fd, 2)
        
        # 运行程序
        program = command.split(' ')[0]
        args = command.split(' ')[1:]

        try:
            os.execvp(program, [program] + args)
        except:
            sys.exit(1)

    def loop(self):
        while True:
            result = self.p.poll()
            for fd, event in result:
                print "Received a child connection"
                try:
                    newsock, addr = self.fd2socket(fd).accept()
                    self.newconn(newsock, self.commands[fd])
                except:
                    pass

host = ''
state = stateclass()

config = open("inetd.txt")
for line in config:
    line = line.strip()
    port, command = line.split(":", 1)
    port = int(port)
      
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((host, port))
    s.listen(1)
    s.setblocking(0)
    state.addmastersock(s, command)

config.close()
state.loop()
