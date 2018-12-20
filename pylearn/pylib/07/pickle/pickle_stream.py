#! /usr/bin/env python
# -*- coding:UTF-8 -*-

try:
    import cPickle as pickle
except:
    import pickle

import pprint
from StringIO import StringIO

class SimpleObject(object):
    def __init__(self,name):
        self.name = name
        self.name_backwards = name[::-1]

data = []
data.append(SimpleObject("pickle"))
data.append(SimpleObject("cPickle"))
data.append(SimpleObject("last"))

out_s = StringIO()

# Pickle
for o in data:
    print "WRITING : %s (%s)" % (o.name, o.name_backwards)
    pickle.dump(o, out_s)
    out_s.flush()

in_s = StringIO(out_s.getvalue())

# Unpickle from in stream
while True:
    try:
        obj = pickle.load(in_s)
    except EOFError:
        break
    else:
        print "READING : %s (%s)" % (obj.name, obj.name_backwards)


