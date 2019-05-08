#! /usr/bin/env python
# -*- coding:utf-8 -*-
#选择并打印位于特定目录下，特定模式的文件中特定模式的行

import os
import time
import fnmatch
import gzip,bz2
import sys


def find_files(topdir, pattern): # 产生一系列文件名
    for path,dirnames,filelist in os.walk(topdir):
        for filename in filelist:
            if fnmatch.fnmatch(filename,pattern):
                yield  os.path.join(path,filename)


def opener(filenames):  # 产生一系列文件对象
    for name in filenames:
        if name.endswith('.gz'):
            f = gzip.open(name)
        elif name.endswith('.bz2'):
            f = bz2.BZ2File(name)
        else:
            f = open(name)
        yield f


def cat(file_olist): # 产生一系列行
    for f in file_olist:
        for line in f:
            yield line


def grep(pattern, lines): # 产生一系列特定模式的行
    for line in lines:
        if pattern in line:
            yield line


if __name__ == '__main__':
    logs = find_files("/var/log", "*log*")
    files = opener(logs)                   
    lines = cat(files)                     
    pylines = grep("python",lines)        
    for line in pylines:
        sys.stdout.write(line)
