#!/usr/bin/env python
# encoding: UTF-8

import threading
import logging

logging.basicConfig( level=logging.DEBUG,
                     format='(%(threadName)-10s) %(message)s',
                    )

class MyThread(threading.Thread):
    
    def run(self):
        logging.debug('Running')

for i in range(5):
    t=MyThread()
    t.start()
