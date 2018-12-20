#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#
# trampoline.py
#
# A simple of example of trampoling between coroutines

# A subroutine
def add(x,y):
    yield x+y

# A function that calls a subroutine
def main():
    r = yield add(2,2)   # 协程嵌套
    print r
    yield

def run(): # 需要自己调度
    m      = main()       
    # An example of a "trampoline"
    sub    = m.send(None)             
    result = sub.send(None)
    m.send(result)

run()
