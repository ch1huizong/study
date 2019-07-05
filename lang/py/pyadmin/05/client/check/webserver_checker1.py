#! /usr/bin/env python3
# -*-coding:utf-8 -*-
# @Time    : 2019/06/14 18:31:02
# @Author  : che
# @Email   : ch1huizong@gmail.com
# 基于Socket的Web服务器检测
# 具体,探测web服务器上的莫个资源是否存在
# 缺点，需要自己构造socket和request

import socket
import re
import sys


def check_webserver(address, port, resource):

    if not resource.startswith("/"):
        resource = "/" + resource
    request = "GET %s HTTP/1.0\r\nHost: %s\r\n\r\n" % (resource, address)
    print("HTTP request:")
    print("|||\n%s\n|||" % request)

    socket.setdefaulttimeout(30)
    s = socket.socket()
    print("Attempting to connect to %s on port %s" % (address, port))
    try:
        s.connect((address, port))
        print("Connected to %s on port %s" % (address, port))
        s.send(request.encode())
        rsp = s.recv(100).decode()
        print("Received 100 bytes of HTTP response")
        print("|||\n%s\n|||" % rsp)
    except socket.error as e:
        print("Connection to %s on port %s failed: %s" % (address, port, e))
        return False  # 网络部分发生异常
    finally:
        print("Closing the connection")
        s.close()

    print("\n")
    lines = rsp.splitlines()
    print("First line of HTTP response: %s" % lines[0])
    try:
        version, status, mesg = re.split("\s+", lines[0], 2)
        print("Version: %s, Status: %s, Message: %s" % (version, status, mesg))
    except ValueError:
        print("Failed to split status line")
        return False  # 解析响应出问题
    if status in ["200", "301"]:
        print("Success - status %s" % status)  # web服务运行正常,且资源正确
        return True
    else:
        print("Status was %s" % status)
        return False  # 状态码出问题


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
    parser.add_option(
        "-r",
        "--resource",
        dest="resource",
        default="index.html",
        help="RESOURCE to check",
        metavar="RESOURCE",
    )
    (options, args) = parser.parse_args()

    print("options: %s, args: %s" % (options, args))
    check = check_webserver(options.address, options.port, options.resource)
    print("check_server returned %s" % check)
    sys.exit(not check)  # 希望从shell脚本调用该方法
