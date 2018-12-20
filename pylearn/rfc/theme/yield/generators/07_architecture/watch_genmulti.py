#!/usr/bin/env python 
# -*- coding:UTF-8 -*-
#
# 监控多个输入源
# 他大爷的！太帅了!
# genmulti.py 
# Generate items from multiple generators (multiplex)
#
import Queue, threading


def gen_multiplex(genlist):
    item_q = Queue.Queue()  # 维护一个全局队列 

    def run_one(source):
        for item in source: item_q.put(item)

    def run_all():
        thrlist = []
        for source in genlist:
            t = threading.Thread(target=run_one,args=(source,))  # 子线程
            t.start()
            thrlist.append(t)

        # 阻塞，等待每一个线程结束,如果一个永不返回，程序一直阻塞
        for t in thrlist: t.join() 
        item_q.put(StopIteration)


    threading.Thread(target=run_all).start() # 父主线程
    while True:
        item = item_q.get()
        if item is StopIteration: return
        yield item


# Example use
#
# This example requires you to perform these setup steps:
#
# 1.  Go to run/foo and run logsim.py
# 2.  Go to run/bar and run logsim.py
#
# These two steps will start writing two different Apache log files.
# Now, we're going to read from both at the same time.

# bug: if one never terminate, the other will always waiting for join?
# 是的！
# Yes!

if __name__ == '__main__':
    from follow import *
    
    log1 = follow(open("run/foo/access-log"))
    log2 = follow(open("run/bar/access-log"))
    
    log = gen_multiplex([log1,log2])
    
    for line in log:
        print line,
