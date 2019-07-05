#! /usr/bin/env python
# -*- coding:UTF-8 -*-
# 并发测试客户端

import socket
import threading
import sys

def work(host, port):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((host, port))

    sys.stdout.write("%s is running: \n"%threading.currentThread())
    s.send("Hello world!")
    while True:
        data = s.recv(1024)
        if not data:
            break
        sys.stdout.write(data)
    s.close()

if __name__ == '__main__':
    host = '192.168.1.100'
    port = 10000
    threads =  []

    for num in range(100):
        t = threading.Thread(target=work, name="Thead: %d"%num, args=(host, port))
        t.daemon = True
        t.start()
        threads.append(t)

    for thread in threads:
        t.join()

