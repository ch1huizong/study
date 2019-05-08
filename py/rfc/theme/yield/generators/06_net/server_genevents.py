#!/usr/bin/env python 
# -*- coding:UTF-8 -*-
#
# genevents.py
#
# A very simplistic example of generating events on a set of sockets

import select
def gen_events(socks):  # 处理客户端业务
    while True:
        rdr,wrt,err = select.select(socks,socks,socks,0.1)
        for r in rdr:
            yield "read",r  # 若换成print
        for w in wrt:
            yield "write",w
        for e in err:
            yield "error",e

# Example use
# Use telnet to port 12000 to test this

if __name__ == '__main__':
    import socket
    from server_genreceive import *

    addr = ("",12000)
    clientset = []   # 共享数据结构,存储client_sock
    def acceptor(sockset,addr):
        for c,a in receive_connections(addr):
            clientset.append(c)

    # 第一部分,服务器部分,接受客户的连接, 作为线程运行
    import threading
    acc_thr = threading.Thread(target=acceptor,
                               args = (clientset, addr))
    acc_thr.setDaemon(True)
    acc_thr.start()
    
    for evt,s in gen_events(clientset): # 第二部分,业务处理部分,处理客户端r/w/e事件
        if evt == 'read':
            data = s.recv(1024)
            if not data:
                print "Closing", s
                s.close()
                clientset.remove(s)
            else:
                print s,data
