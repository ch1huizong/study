#! /usr/bin/env python3
# -*-coding:UTF-8 -*-
# @Time    : 2019/01/03 15:50:19
# @Author  : che
# @Email   : ch1huizong@gmail.com

from threading import Thread
import time
import socket


class CountdownTask(object):

    def __init__(self):
        self._running = True

    def terminate(self):
        self._running = False

    def run(self, n):
        while self._running and n > 0:
            print('T-minus', n)
            n -= 1
            time.sleep(5)


class IOTask(object):

    def terminate(self):
        self._running = False

    def run(self, sock):
        sock.settimeout(5)
        while self._running:
            try:
                data = sock.recv(8192)
            except socket.timeout:
                continue
        return


if __name__ == '__main__':
    c = CountdownTask()
    t = Thread(target=c.run, args=(10,))
    t.start()
    c.terminate()
    t.join()
