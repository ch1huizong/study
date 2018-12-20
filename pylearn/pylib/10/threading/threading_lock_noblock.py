#!/usr/bin/env python
# encoding: UTF-8

import threading
import logging
import time

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )


def lock_holder(lock):
    logging.debug('Start')
    while True:
        lock.acquire()
        try:
            logging.debug('Holding')
            time.sleep(0.5)
        finally:
            logging.debug('Not holding')
            lock.release()
        time.sleep(0.5)

def worker(lock):
    logging.debug('Starting')
    num_tries=0
    num_acquires=0
    while num_acquires<3:
        time.sleep(0.5)
        logging.debug('Trying to acquire')
        flag=lock.acquire(0)    ####Note ,not block
        try:
            num_tries+=1
            if flag:
                logging.debug('Iteration:%d Acquired.'%num_tries)
                num_acquires+=1
            else:
                logging.debug('Iteration:%d Not Acquired.'%num_tries)
        finally:
            if flag:
                lock.release()

    logging.debug('Done after %d iterations',num_tries)

lock=threading.Lock()

holder=threading.Thread(target=lock_holder,args=(lock,),name="Hold_locker")
holder.setDaemon(True)
holder.start()

worker=threading.Thread(target=worker,args=(lock,),name="Worker")
worker.start()
