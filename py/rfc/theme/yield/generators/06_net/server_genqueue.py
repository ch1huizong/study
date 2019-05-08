#!/usr/bin/env python 
# -*- coding:UTF-8 -*-
#
# genqueue.py
#
# Generate a sequence of items that put onto a queue
#
# 启发: 
# 生产者消费者在一个文件里，可以引用同一个队列; 如若在两者分布在网络上？
#

def consume_queue(thequeue):
    while True:
        item = thequeue.get()  # block 
        if item is StopIteration: break # 这里会关闭生成器自身
        yield item

# Example
if __name__ == '__main__':
    import Queue, threading
    def consumer(q): # 消费者
        for item in consume_queue(q):
            print "Consumed", item
        print "done"

    in_q = Queue.Queue() # 共享队列
    con_thr = threading.Thread(target=consumer,args=(in_q,))  # 消费者进程
    con_thr.start()

    # Now, pipe a bunch of data into the queue
    for i in xrange(10000):
        in_q.put(i)
    in_q.put(StopIteration)
