#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time
import sys


#读取文件对象，产生生成器对象
def tail(f):
    f.seek(0,2)
    while True: 
        line = f.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line


#协程，打印包含特定模式的行，等待发送给它的信号
def print_matches(matchtext):
    print"Looking for",matchtext
    while True:
        line = (yield)
        if matchtext in line:
            print line,


def test():
    # 一组匹配器协程
    matchers = [ 
        print_matches("python"),
        print_matches("guido"),
        print_matches("jython"),
    ]

    # 通过调用next准备所有的匹配器
    for m in matchers:
        m.next()
        
    #输入特定的测试文件  
    filename = sys.argv[1]

    #开始工作
    for line in tail(open(testfile)):
        for m in matchers:  # 将数据发送至每一个匹配器协程中, 类似广播
            m.send(line)


if __name__ == '__main__':
    test()
