#! /usr/bin/env python3
# -*-coding:utf-8 -*-
# @Time    : 2019/06/14 18:05:18
# @Author  : che
# @Email   : ch1huizong@gmail.com
# TCP端口检查

import socket
import re
import sys


def check_server(address, port):
    socket.setdefaulttimeout(30)
    s = socket.socket()
    print("Attempting to connect to %s on port %s" % (address, port))
    try:
        s.connect((address, port))
        print("Connected to %s on port %s" % (address, port))
        return True
    except socket.error as e:
        print("Connection to %s on port %s failed: %s" % (address, port, e))
        return False


if __name__ == "__main__":
    from optparse import OptionParser

    parser = OptionParser()

    parser.add_option(
        "-a",
        "--address",
        dest="address",
        default="localhost",
        help="ADDRESS for server",
        metavar="ADDRESS",
    )
    parser.add_option(
        "-p",
        "--port",
        dest="port",
        type="int",
        default=80,
        help="PORT for server",
        metavar="PORT",
    )
    (options, args) = parser.parse_args()

    print("options: %s, args: %s" % (options, args))
    check = check_server(options.address, options.port)
    print("check_server returned %s" % check)
    sys.exit(not check)  # 取反check_server返回值给shell
