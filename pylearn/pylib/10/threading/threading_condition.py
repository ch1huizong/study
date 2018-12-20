#!/usr/bin/env python
# encoding: UTF-8

import logging
import threading
import time

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s (%(threadName)-2s)  %(message)s'
    )

def consumer(cond):
    logging.debug('Starting consumer thread.')
    with cond:
        cond.wait()
        logging.debug('Resource is available to consumer')

def producer(cond):
    logging.debug('Starting producer thread.')
    with cond:
        logging.debug('Making resource available')
        cond.notifyAll()

condition=threading.Condition()

c1=threading.Thread(target=consumer,args=(condition,),name='c1')
c2=threading.Thread(target=consumer,args=(condition,),name='c2')
p=threading.Thread(target=producer,args=(condition,),name='p')

c1.start()
time.sleep(2)
c2.start()
time.sleep(2)
p.start()

        
