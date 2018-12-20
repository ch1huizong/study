#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 全局变量控制是否跟踪调试
enable_tracing = True
if enable_tracing: 
    debug_log = open('debug.log','w')

# 装饰器函数
def trace(func):
    if enable_tracing:
        def callf(*args, **kwargs): # 注意一下参数,其实是函数接口
            debug_log.write('Calling %s: %s, %s\n' % (func.__name__, args, kwargs))
            r = func(*args,**kwargs)
            debug_log.write('%s returned %s\n' % (func.__name__, r))
            return r
        return callf
    else:
        return func


@trace
def square(x):
    return x * x


# ex1, 接收参数的装饰器
@eventhandler('BUTTON')
def handle_button(msg):
    pass


def handle_button(msg):
    pass
temp = eventhandler('BUTTON')
handle_button = temp(handle_button)


# ex2
event_handlers = {}  
def eventhandler(event): 
    def register_function(f):  # 进一步的装饰器了
        event_handlers[event] = f
        return f
    return register_function


# 类装饰器, 必须始终返回类对象
@foo
class Bar(object):
    def __init__(self, x):
        self.x = x
    def spam(self):
        pass
