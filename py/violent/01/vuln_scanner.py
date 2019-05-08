#! /usr/bin/env python3
# -*-coding:UTF-8 -*-
# @Time    : 2019/04/12 18:19:08
# @Author  : che
# @Email   : ch1huizong@gmail.com

import sys
import os
import socket


def ret_banner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(1024)
    except Exception as e:
        banner = None
    return banner


def check_vulns(banner, filename):
    with open(filename, "rb") as f:
        for line in f:
            if line.strip() in banner:
                print("[+] Server is vulnerable:" + banner.strip())


def main():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        if not os.path.isfile(filename):
            print("[-] %s does not exist." % filename)
            return
        if not os.access(filename, os.R_OK):
            print("[-] %s access denied." % filename)
            return
    else:
        print("[-] Usage: %s <vuln_filename>" % sys.argv[0])
        return

    port_list = [21, 22, 25, 80, 110, 443]
    for x in range(1, 255):
        ip = "192.168.1." + str(x)
        for port in port_list:
            #print('[+] Checking %s: %s' % (ip, port))
            banner = ret_banner(ip, port)
            if banner:
                print("[+] %s: %s" % (ip, banner))
                check_vulns(banner, filename)


if __name__ == "__main__":
    main()
