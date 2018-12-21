#! /usr/bin/env python3
# -*-coding:UTF-8 -*-
# @Time    : 2018/12/21 18:29:16
# @Author  : che
# @Email   : ch1huizong@gmail.com
# 自己定义线程的终止条件

import threading


class StoppableThread(threading.Thread):

    def __init__(self):
        super().__init__()
        self._terminate = False
        self._suspend_lock = threading.Lock()

    def terminate(self):
        self._terminate = True

    def suspend(self):
        self._suspend_lock.acquire() 
        
    def resume(self):
        self._suspend_lock.release() 

    def run(self):
        while True:
            if self._terminate:
                break
            self._suspend_lock.acquire()
            self._suspend_lock.release()
            pass
