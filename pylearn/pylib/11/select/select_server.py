#! /usr/bin/env python
# -*- coding:UTF-8 -*-

import socket
import select
import sys
import Queue

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setblocking(0)

server_address = ('localhost',10000)
print >> sys.stderr, "starting up on %s port %s"% server_address
server.bind(server_address)
server.listen(5)

# select初始化
inputs = [ server ]
outputs = []
message_queues = {}

while inputs:
    print >> sys.stderr, "waiting for the next event..."
    timeout = 1             # 引入超时
    readable, writable, exceptional = select.select(inputs, 
                                        outputs, 
                                        inputs,
                                        timeout
                                        )
    if not ( readable or writable or exceptional ):
        print >> sys.stderr, "    time out, do some other work here."
        continue

    #处理输入
    for s in readable:
        if s is server:    # 服务器套接字
            connection, client_address = s.accept()
            print >> sys.stderr, "  connetion from", client_address
            connection.setblocking(0)
            inputs.append(connection)
            message_queues[connection] = Queue.Queue()  # 每一个连接一个queue
        else:
            data = s.recv(1024)		#客户端套接字,可以保证数据被接受完
            if data:                    # 有数据到达的客户端套接字
                print >> sys.stderr, "    received '%s' from %s "%\
                        (data, s.getpeername())
                message_queues[s].put(data)
                if s not in outputs:
                    outputs.append(s)
            else:                               #没有数据了
                print >> sys.stderr, "    closing",client_address
                if s in outputs:
                    outputs.remove(s)
                inputs.remove(s)
                s.close()

                del message_queues[s]

    # 处理输出
    for s in writable:
        try:
            next_msg = message_queues[s].get_nowait()
        except Queue.Empty:
            print >> sys.stderr, '    ',s.getpeername(),'queue empty'
            outputs.remove(s)
        else:
            print >> sys.stderr, "    sending %s to %s"%\
                    (next_msg, s.getpeername())
            s.send(next_msg)

    #处理错误
    for s in exceptional:
        print >> sys.stderr, "exception condition on",s.getpeername()
        # 清除在输入列表中的监听
        inputs.remove(s)
        if s in outputs:
            outputs.remove(s)
        s.close()

        del message_queues[s]







