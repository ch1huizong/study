#!/usr/bin/env python 
# -*- coding:UTF-8 -*-
# threadsend.py
#
# Send items to consumer threads

import Queue, threading

class ConsumerThread(threading.Thread):

    def __init__(self,target):
        threading.Thread.__init__(self)
        self.setDaemon(True)
        self.in_queue = Queue.Queue() # 维护自己的一个内部队列
        self.target = target

    def send(self,item):
        self.in_queue.put(item)

    def generate(self):
        while True:
            item = self.in_queue.get()  # 阻塞
            yield item

    def run(self):  # 相当于 for item in genitems: process(item)
        self.target(self.generate())

# Example Use

if __name__ == '__main__':
    from follow import *
    from apachelog import *
    from broadcast import *
    
    def find_404(log):
        r404 = (r for r in log if r['status'] == 404)
        for r in r404:
            print r['status'],r['datetime'],r['request']

    def bytes_transferred(log):
        total = 0
        for r in log:
            total += r['bytes']
            print "Total bytes", total
            
    c1 = ConsumerThread(find_404)
    c1.start()
    c2 = ConsumerThread(bytes_transferred)
    c2.start()
    
    lines = follow(open("run/foo/access-log"))
    log   = apache_log(lines)
    broadcast(log,[c1,c2])
