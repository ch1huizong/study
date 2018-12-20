#! /usr/bin/env python
# -*- coding:UTF-8 -*-

import Pyro.core
import os

class PSACB(object):    # 服务端记录了的对象类型

    def __init__(self):
        self.name = 1

    def cb(self):   # 对象的方法
        return "PSA callback"


class PSAExample(Pyro.core.ObjBase):
    
    def ls(self, directory):
        try:
            return os.listdir(directory)
        except OSError:
            return []

    def ls_boom(self, directory):
        return os.listdir(directory)

    def cb(self, obj):
        print "OBJECT::", obj
        print "OBJECT.__class__::", obj.__class__
        return obj.cb()

if __name__ == '__main__':
    Pyro.core.initServer()
    daemon = Pyro.core.Daemon()
    uri = daemon.connect(PSAExample(), 'psaexample')

    print 'The daemon runs on port:', daemon.port
    print 'The object"s uri is:', uri
    daemon.requestLoop()
