#!/usr/bin/env python 
# -*- coding:UTF-8 -*- 
# storelast.py
#
# An iterator that stores the last value returned.  

# 自己实现了迭代器协议，即可迭代又可保存数据
class storelast(object): 

    def __init__(self,source):
        self.source = source

    def next(self):
        item = self.source.next()
        self.last = item  #存储最后一个条目
        return item

    def __iter__(self):
        return self

# Example
if __name__ == '__main__':
    from follow import *
    from apachelog import *

    lines = storelast(follow(open("run/foo/access-log")))
    log   = apache_log(lines)


    for r in log: # 驱动
        print r
        # lines是一个固定对象，随着迭代lines.last一直在改变
        print lines.last  
