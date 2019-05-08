#! /usr/bin/env python
# -*- coding:UTF-8 -*-
# 自定义对象obj传递在Pyro和xmlrpcserver上的不同

import Pyro.core
import xmlrpclib

class PSACB(object):    # 传递给rpc服务器上的对象, 服务端需要有class定义

    def __init__(self):
        self.name = 1

    def cb(self):   # 对象的方法
        return "PSA callback"

if __name__ == '__main__':
    cb = PSACB()
    
    print "PYRO SECTION"
    print "*" * 20
    psapyro = Pyro.core.getProxyForURI('PYRO://127.0.1.1:7766/7f00010161d216e429b8bfcc632ed987') 
    print "-->>", psapyro.cb(cb)

    print "XML-RPC SECTION"
    print "*" * 20
    psaxmlrpc = xmlrpclib.ServerProxy('http://localhost:8765')
    print "-->>", psaxmlrpc.cb(cb)
    print "*" * 20
