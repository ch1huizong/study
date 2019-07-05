#! /usr/bin/env python3
# -*-coding:utf-8 -*-
# @Time    : 2019/06/15 10:27:17
# @Author  : che
# @Email   : ch1huizong@gmail.com

import os
import Pyro4


class PSACB(object): # 服务端记录了的对象类型
    def __init__(self):
        self.name = 1

    def cb(self):  # 对象的方法
        return "PSA callback"


@Pyro4.expose
class PSAExample(object):
    def ls(self, directory):
        try:
            return os.listdir(directory)
        except OSError:
            return []

    def ls_boom(self, directory):
        return os.listdir(directory)

    def cb(self, obj):
        print("OBJECT::", obj)
        print("OBJECT.__class__::", obj.__class__)
        return obj.cb()


if __name__ == "__main__":
    daemon = Pyro4.Daemon()
    uri = daemon.register(PSAExample, "psaexample")
    #print("The daemon runs on port:", daemon.port)
    print('The object"s uri is:', uri)
    daemon.requestLoop()
