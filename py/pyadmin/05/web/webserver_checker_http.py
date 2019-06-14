#! /usr/bin/env python3
# -*-coding:utf-8 -*-
# @Time    : 2019/06/14 19:01:30
# @Author  : che
# @Email   : ch1huizong@gmail.com
# 基于httplib的Web服务器检测

import sys
import socket
import http.client


def check_webserver(address, port, resource):
    if not resource.startswith("/"):
        resource = "/" + resource

    try:
        conn = http.client.HTTPConnection(address, port)
        print("HTTP connection created successfully") # 小bug

        req = conn.request("GET", resource)
        print("request for %s successful" % resource)

        response = conn.getresponse()
        print("respose status: %s" % response.status)
        print("\n")

    except socket.error as e:  # 网络问题
        print("HTTP connection failed: %s" % e)
        return False
    finally:
        conn.close()
        print("HTTP connection closed successfully")

    if response.status in [200, 301]:
        return True
    else:
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
