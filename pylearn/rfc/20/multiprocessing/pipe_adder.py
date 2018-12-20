#!/usr/bin/env python
# -*- coding:UTF-8
# 管道双向通信

import multiprocessing

#服务器端
def adder(pipe):
    server_p,client_p = pipe
    client_p.close()
    while True:
        try:
            x,y = server_p.recv()
        except EOFError:
            break
        result = x + y
        server_p.send(result)     #也可以发送数据? 是的
    print'Server done'

if __name__ == '__main__':
    #创建管道
    server_p,client_p = multiprocessing.Pipe()
    #服务器
    serv_p = multiprocessing.Process(target=adder, \
                        args=((server_p,client_p),))
    serv_p.start()

    #父进程产生数据
    server_p.close()
    client_p.send([3,4])

    print client_p.recv()   #也可接收? 是的
    client_p.send(['hello','world'])
    print client_p.recv()

    #关闭客户端
    client_p.close()
    #等待服务器进程结束
    serv_p.join()

