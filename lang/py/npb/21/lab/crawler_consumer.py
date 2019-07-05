#! /usr/bin/env python
# -*- coding:UTF-8 -*-
# 基于生产者-消费者模型的多线程页面抓取

import time
import threading
import Queue
import urllib2

class Consumer(threading.Thread):
    def __init__(self,queue):
        threading.Thread.__init__(self)
        self._queue = queue

    def run(self):
        while True:
            item = self._queue.get()
            if isinstance(item,str) and item == 'quit':
                break
            response = urllib2.urlopen(item)
            # self._queue.task_done()  # 对应的是queue.join语句，与这里不符
        #self._queue.task_done()
        print "Bye bye"


def build_worker_poll(queue, size):
    workers = []

    for _ in range(size):
        worker = Consumer(queue)
        worker.start()
        workers.append(worker)
    return workers


class Producer():
    urls = [ "http://www.baidu.com",
             "http://www.douban.com",
             "http://www.zhihu.com",
             "http://www.python.org",
             "http://www.sohu.com",
             "http://www.sina.com.cn",
             "http://www.ifeng.com",
             "http://www.qq.com",
            ]

    queue = Queue.Queue()
    worker_threads = build_worker_poll(queue,4)
    start_time = time.time()

    for url in urls:
        queue.put(url)
    for worker in worker_threads:
        queue.put("quit")

    for worker in worker_threads:
        worker.join()   # 这里是Thread.join

    #queue.join()       # 若在队列上应用join,消费者需要task_done方法

    print"Done! Time taken: {}".format(time.time()-start_time)

if __name__ == '__main__':
    Producer()

