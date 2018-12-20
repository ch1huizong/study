#! /usr/bin/env python
# -*- coding:UTF-8 -*-

# 把对象pickle至文件

try:
    import cPickle as pickle
except:
    import pickle
import sys


class SimpleObject(object):
    def __init__(self,name):
        self.name = name
        self.name_backwards = name[::-1]

if __name__ == '__main__':
    data = []
    data.append(SimpleObject("pickle"))
    data.append(SimpleObject("cPickle"))
    data.append(SimpleObject("last"))

    filename = sys.argv[1]
    
    with open(filename, 'wb') as f:
        for o in data:
            print "WRITING : %s (%s)" % (o.name, o.name_backwards)
            pickle.dump(o, f)
