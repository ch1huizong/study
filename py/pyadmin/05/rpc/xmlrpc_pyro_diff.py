#! /usr/bin/env python3
# -*-coding:utf-8 -*-
# @Time    : 2019/06/15 10:57:20
# @Author  : che
# @Email   : ch1huizong@gmail.com
# 自定义对象obj传递在Pyro和xmlrpcserver上的不同

import xmlrpc.client
import Pyro4


class PSACB(object):  # 传递给rpc服务器上的对象, 服务端需要有class定义
    def __init__(self):
        self.name = 1

    def cb(self):  # 对象的方法
        return "PSA callback"


if __name__ == "__main__":

    cb = PSACB()

    print("PYRO SECTION")
    print("*" * 20)
    psapyro = Pyro4.Proxy("PYRO:psaexample@localhost:43095")
    print("-->>", psapyro.cb(cb))

    print("XML-RPC SECTION")
    print("*" * 20)
    psaxmlrpc = xmlrpc.client.ServerProxy("http://localhost:8765")
    print("-->>", psaxmlrpc.cb(cb))
    print("*" * 20)
