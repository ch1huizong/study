#! /usr/bin/env python3
# -*-coding:utf-8 -*-
# @Time    : 2019/06/15 15:18:15
# @Author  : che
# @Email   : ch1huizong@gmail.com

from twisted.spread import pb
from twisted.internet import reactor


def handle_err(reason):
    print("An error occurred", reason)
    reactor.stop()


def call_ls(def_call_obj):
    return def_call_obj.callRemote("ls_boom", "/foo")  # 会在服务器端引发错误


def print_ls(print_result):
    print(print_result)
    reactor.stop()


if __name__ == "__main__":
    factory = pb.PBClientFactory()
    reactor.connectTCP("localhost", 9876, factory)
    d = factory.getRootObject()
    d.addCallback(call_ls)
    d.addCallback(print_ls)
    d.addErrback(handle_err)
    reactor.run()
