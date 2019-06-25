#! /usr/bin/env python3
# -*-coding:utf-8 -*-
# @Time    : 2019/06/16 16:44:29
# @Author  : che
# @Email   : ch1huizong@gmail.com
# 多队列和多线程池, 会把活动的结果加入到arping队列

import re
from threading import Thread
import subprocess
from queue import Queue

num_ping_threads = 3
num_arp_threads = 3
in_queue = Queue()
out_queue = Queue()
ips = ["192.168.1.%d" % ip for ip in range(1, 255)]


def pinger(i, iq, oq):
    while True:
        ip = iq.get()
        # print('Thread %s: Pinging %s' % (i, ip))
        ret = subprocess.call(
            "ping -c1 %s " % ip,
            shell=True,
            stdout=open("/dev/null", "w"),
            stderr=subprocess.STDOUT,
        )

        if ret == 0:
            oq.put(ip)
        else:
            pass
            # print("%s: did not respond" % ip)
        iq.task_done()


def arping(i, oq):
    while True:
        ip = oq.get()
        p = subprocess.Popen(
            "arping -I wlp3s0 -c5 %s" % ip, shell=True, stdout=subprocess.PIPE
        )
        out = p.stdout.read().decode()

        # 提取mac地址
        result = out.split()
        pattern = re.compile(":")
        macaddr = None
        for item in result:
            if re.search(pattern, item):
                macaddr = item
                break
        print("IP Address: %s | Mac Address: %s" % (ip, macaddr))
        oq.task_done()


def main():
    # 创建ping线程池
    for i in range(num_ping_threads):
        worker = Thread(target=pinger, args=(i, in_queue, out_queue))
        worker.setDaemon(True)
        worker.start()

    # 创建arping线程池
    for i in range(num_arp_threads):
        worker = Thread(target=arping, args=(i, out_queue))
        worker.setDaemon(True)
        worker.start()

    # 向队列添加任务
    for ip in ips:
        in_queue.put(ip)

    print("Main Thread Waiting")
    in_queue.join()  # 两种线程通过queue传递
    out_queue.join()
    print("Done")


main()
