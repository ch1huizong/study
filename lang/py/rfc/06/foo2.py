#!/usr/bin/env python
# -*- coding:utf-8 -*-

import foo1

def bar():
    x = 1122
    def helloworld():
        return "Hello World. x id %d" % x
    v = foo1.callf(helloworld) # 环境和函数打包 
    print(v)

bar()
