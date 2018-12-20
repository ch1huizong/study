#!/usr/bin/env python
# encoding: UTF-8

import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )

def daemon():
    logging.debug('Starting')
    time.sleep(30)
    logging.debug('Exiting')

def non_daemon():
    logging.debug('Starting')

    logging.debug('Exiting')

t=threading.Thread(name='daemon',target=daemon)
t.setDaemon(True)
w=threading.Thread(name='non-daemon',target=non_daemon)

t.start()
w.start()
print'Main exit'

t.join()
w.join()
