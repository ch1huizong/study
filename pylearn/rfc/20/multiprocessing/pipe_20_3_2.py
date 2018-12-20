#!/usr/bin/env python3
# -*- coding:UTF-8

""" 使用管道进行进程间通信 

读端-写端,类似与socket端口
每个端口即可以读入又可以写入
"""

import multiprocessing


def consumer(pipe):
    read_p, write_p = pipe
    write_p.close() # 关闭管道的写端
    while True:
        try:
            item = read_p.recv()
        except EOFError:
            break
        print(item)
    print('Consumer done')


def producer(seq,write_p):
    for item in seq:
        write_p.send(item)

if __name__ == '__main__':
    (read_p, write_p) = multiprocessing.Pipe()
    
    #消费者
    cons_p = multiprocessing.Process(target=consumer, args=((read_p, write_p),))
    cons_p.start()
    
    #关闭父进程的读端
    read_p.close()

    seq = range(100)
    producer(seq, write_p)

    # 生产完成，关闭生产者的写端
    # 否则，会在消费者的recv处阻塞挂起,important
    write_p.close() 

    #等待消费者结束
    cons_p.join()
    print('Main process over')
