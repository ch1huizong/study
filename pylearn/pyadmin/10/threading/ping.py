#! /usr/bin/env python
# -*- coding:UTF-8 -*-

from threading import Thread
import subprocess
from Queue import Queue

num_threads = 3
queue = Queue()
ips = ['192.168.1.%d' % ip for ip in xrange(1, 255)] 

def pinger(i, q): # 实际工作
    while True:
        ip = q.get()
        #print 'Thread %s: Pinging %s' % (i, ip)
        ret = subprocess.call(
            'ping -c1 %s ' %ip,
            shell=True,
            stdout=open('/dev/null', 'w'),
            stderr=subprocess.STDOUT
        )
        
        if ret == 0:
            print "%s: is alive" % ip
        #else:
            #print "%s: did not respond" % ip
        q.task_done() # 完成一个任务


def main():
    # 创建线程池
    for i in range(num_threads):
        worker = Thread(target=pinger, args=(i, queue))
        worker.setDaemon(True)  # 设置为后台进程
        worker.start() # 开启

    # 向队列添加任务
    for ip in ips:
        queue.put(ip) 

    print "Main Thread Waiting"
    queue.join()  # 主线程阻塞，等待队列处理完毕
    print "Done"

# 注意，线程之间的切换调度是操作系统管理的
main()
