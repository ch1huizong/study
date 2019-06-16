#! /usr/bin/env python3
# -*-coding:utf-8 -*-
# @Time    : 2019/06/16 19:08:39
# @Author  : che
# @Email   : ch1huizong@gmail.com

import time
import sys
import subprocess
from multiprocessing import Process, Queue

q = Queue()
ips = ["192.168.0.%d" % ip for ip in range(1, 255)]


def f(i, q):
    while True:
        if q.empty():
            sys.exit()
        print("Process Number: %s" % i)
        ip = q.get()
        ret = subprocess.call(
            "ping -c1 %s" % ip,
            shell=True,
            stdout=open("/dev/null", "w"),
            stderr=subprocess.STDOUT,
        )
        if ret == 0:
            print("%s: is alive" % ip)
        else:
            pass
            #print("Process Number: %s didn't find a response for %s" % (i, ip))


for ip in ips:
    q.put(ip)

for i in range(50):
    p = Process(target=f, args=[i, q])
    p.start()

print("Main process joins on queue")
p.join()  # 没这个方法 
print("Main program finished")
