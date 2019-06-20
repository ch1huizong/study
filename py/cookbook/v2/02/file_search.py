#! /usr/bin/env python
# -*- coding:UTF-8 -*-

"""有点类unix中的find命令"""

import os
import glob

def search_file_byname(filename, search_path, pathsep=os.pathsep):
    """给定搜索路径，按文件名搜索文件,找到第一个就停"""   # 搜索路径/usr:/bin et.
    for path in search_path.split(pathsep):
        if os.path.isfile(os.path.join(path,filename)):
            return os.path.abspath(os.path.join(path,filename))
    return None

def test1():
    search_path = '/bin' + os.pathsep + '/usr/bin'
    find_file = search_file_byname('ls', search_path)
    if find_file:
        print "File 'ls' found at %s" % find_file
    else:
        print "File 'ls' not found" 



def search_file_bypattern(pattern, search_path, pathsep=os.pathsep):
    """给定搜索路径，寻找所有符合模式的文件"""
    for path in search_path.split(pathsep):
        for match in glob.glob(os.path.join(path,pattern)):
            yield match

def test2():
    for m in search_file_bypattern('*.py', os.environ['PATH']):
        print m



test1()
test2()





