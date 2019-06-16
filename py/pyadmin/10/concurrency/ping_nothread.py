#! /usr/bin/env python3
# -*-coding:utf-8 -*-
# @Time    : 2019/06/16 16:05:57
# @Author  : che
# @Email   : ch1huizong@gmail.com

import subprocess
import time

IP_LIST = ["baidu.com", "sohu.com", "douban.com", "amazon.com", "yahoo.com", "freebase"]

cmd_stub = "ping -c5 %s"


def do_ping(addr):
    print(time.asctime(), "DOING PING FOR", addr)
    cmd = cmd_stub % addr
    return subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)


def main():
    z = []
    for ip in IP_LIST:
        p = do_ping(ip)
        z.append((p, ip))

    for p, ip in z:
        print(time.asctime(), "WAITING FOR", ip)
        p.wait()  # 这样的话，就有等待顺序
        print(time.asctime(), ip, "RETURNED", p.returncode)


if __name__ == "__main__":
    main()
