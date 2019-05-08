#!/usr/bin/env python
# encoding: UTF-8

import threading
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )

def work_with(lock):
    with lock:
        logging.debug('Lock acquired via with')

def work_no_with(lock):
    lock.acquire()
    try:
        logging.debug('Lock acquired directly')
    finally:
        lock.release()

lock=threading.Lock()
w=threading.Thread(target=work_with,args=(lock,))
nw=threading.Thread(target=work_no_with,args=(lock,))

w.start()
nw.start()


