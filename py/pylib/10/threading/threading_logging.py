#!/usr/bin/env python
# encoding: UTF-8

import threading,time
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
    )

def worker():
    logging.debug('Starting')
    time.sleep(2)
    logging.debug('Exiting')

def my_service():
    logging.debug('Starting')
    time.sleep(3)
    logging.debug('Exiting')

t=threading.Thread(name='My_service',target=my_service)
w=threading.Thread(name='worker',target=worker)
wd=threading.Thread(target=worker)

t.start()
w.start()
wd.start()
    
