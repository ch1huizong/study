#!/usr/bin/env python
# -*-coding:UTF-8 -*-
# 使用进程池，可以对任务序列进行分割

import os
import multiprocessing
import hashlib
import sys
from itertools import ifilter

BUF = 512 
POOLSIZE = 4 

def compute_digest(filename):  #计算文件的hash值
    try:
        f = open(filename,'rb')
    except IOError:
        return None
    digest = hashlib.sha512()
    while True:
        chunk = f.read(BUF)
        if not chunk: break
        digest.update(chunk)
    f.close()
    return filename,digest.hexdigest()   #元组

def build_digest_map(topdir):     
    p = multiprocessing.Pool(POOLSIZE)   #工作池
    allfiles = ( os.path.join(path,name) 
                    for path, dirs,files in os.walk(topdir)
                        for name in files
                )
    
    digest_map = dict(ifilter(None,p.imap_unordered(compute_digest,allfiles,20)))
    p.close()
    
    return dict(digest_map)

if __name__ == '__main__':
    digest_map = build_digest_map("/root")  # 为何根目录不行？
    for line, key in enumerate(digest_map):
        print "%d : %s -> %s\n" % (line, key, digest_map.get(key))

    print len(digest_map)
