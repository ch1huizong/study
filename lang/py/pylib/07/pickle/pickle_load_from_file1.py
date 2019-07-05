#! /usr/bin/env python
# -*- coding:UTF-8 -*-
# unpickle时需要有实例对象的类

try:
    import cPickle as pickle
except:
    import pickle
import sys
from pickle_dump_to_file1 import SimpleObject

filename = sys.argv[1]

with open(filename,'rb') as f:
    while True:
        try:
            obj = pickle.load(f)
        except EOFError:
            break
        else:
            print "READING : %s (%s)" % (obj.name, obj.name_backwards)


