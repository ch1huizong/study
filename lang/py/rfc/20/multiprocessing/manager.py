#!/usr/bin/env python
# -*- coding:utf-8 -*-

import multiprocessing
import time

#只要设定要传递的事件，就打印d
def watch(d,evt):
    while True:
        evt.wait()
        print d
        evt.clear()

if __name__ == '__main__':
    m = multiprocessing.Manager()
    d = m.dict()
    evt = m.Event()

    #启动监视字典的进程
    p = multiprocessing.Process(target=watch,args=(d,evt))
    p.daemon = True
    p.start()

    #更新字典并通知监视者
    d['foo'] = 42
    evt.set()
    time.sleep(5)

    d['bar'] = 'hello'
    evt.set()
    time.sleep(5)

    #终止进程和管理器
    p.terminate()
    m.shutdown()


