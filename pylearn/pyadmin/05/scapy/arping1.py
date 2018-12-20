#! /usr/bin/env python
# -*- coding:UTF-8 -*-
# 特定平台arp工具 

import subprocess
import re
import sys

def arping(ipaddress="192.168.1.1"):
    p = subprocess.Popen("arping -c2 %s" % ipaddress, shell=True, stdout=subprocess.PIPE)
    out = p.stdout.read()
    result = out.split()
    #print(result)

    for item in result:
        if ":" in item:
            print item
            break

if __name__ == '__main__':

    if len(sys.argv) > 1:
        for ip in sys.argv[1:]:
            print "arping", ip
            arping(ip)
    else:
        arping()
