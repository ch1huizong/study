#! /usr/bin/env python
# -*- coding:UTF-8 -*-
# 基于线程池的页面爬取

import urllib2
from multiprocessing.dummy import Pool as ThreadPool
import time

urls = [ "http://www.baidu.com",
         "http://www.douban.com",
         "http://www.zhihu.com",
         "http://www.python.org",
         "http://www.sohu.com",
         "http://www.sina.com.cn",
         "http://www.ifeng.com",
         "http://www.qq.com",
        ]

results = []
start_time = time.time()
for url in urls:
    result = urllib2.urlopen(url)
    results.append(result)
print "%20s: %s"%("Single thread",time.time()-start_time)
    

start_time = time.time()
pool = ThreadPool(4)
results = pool.map(urllib2.urlopen, urls)
print "%20s: %s"%("4 thread",time.time()-start_time)


start_time = time.time()
pool = ThreadPool(8)
results = pool.map(urllib2.urlopen, urls)
print "%20s: %s"%("8 thread",time.time()-start_time)

start_time = time.time()
pool = ThreadPool(13)
results = pool.map(urllib2.urlopen, urls)
print "%20s: %s"%("13 thread",time.time()-start_time)


#pool.close()
#pool.join()
