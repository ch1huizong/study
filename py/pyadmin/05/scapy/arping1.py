#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# 特定平台arp工具

import subprocess
import re
import sys


def arping(ipaddress="192.168.0.1"):
    p = subprocess.Popen(
        "arping -I wlp3s0 -c2 %s" % ipaddress, shell=True, stdout=subprocess.PIPE
    )
    out = p.stdout.read().decode()
    result = out.split()

    for item in result:
        if ":" in item:
            print(item)


if __name__ == "__main__":

    if len(sys.argv) > 1:
        for ip in sys.argv[1:]:
            print("arping", ip)
            arping(ip)
    else:
        arping()
