#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 基于协程的grepline,可以作为一个原型，很重要

import os
import sys
import fnmatch
import gzip,bz2


# 协程装饰器
def coroutine(func):
    def start(*args,**kwargs):
        g = func(*args,**kwargs)
        g.next()
        return g
    return start


@coroutine
def find_files(target):  # 接收目录和文件模式
    while True:
        topdir, pattern = (yield)    #注意!
        for path,dirnames,filelist in os.walk(topdir):
            for filename in filelist:
                if fnmatch.fnmatch(filename,pattern):
                    target.send(os.path.join(path,filename))


@coroutine
def opener(target): # 接收一系列文件名
    while True:
        name = (yield)
        if name.endswith('.gz'):
            f = gzip.open(name)
        elif name.endswith('.bz2'):
            f = bz2.BZ2File(name)
        else:
            f = open(name)
        target.send(f)


@coroutine
def cat(target):            
    while True:
        f = (yield) # 接收一系列文件句柄
        for line in f:
            target.send(line)


@coroutine
def grep(pattern,target): 
    while True:
        line = (yield)  # 接收一系列特定模式的行
        if pattern in line:
            target.send(line) 


@coroutine
def printer():
    while True:
        line = (yield) # 接收文件行
        sys.stdout.write(line)


if __name__ == '__main__':
    finder = find_files(opener(cat(grep("python",printer()))))
    finder.send(("/var/log","*log*"))
