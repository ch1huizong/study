#! /usr/bin/env python
# -*- coding:UTF-8 -*-
# 数据文件完整性验证
# C-S 两端需要有协议，读取到正确的数据字节

import hashlib
import hmac
try:
    import cPickle as pickle
except:
    import pickle
import pprint
from StringIO import StringIO

def make_digest(message):
    hash = hmac.new("quiet",
                    message,
                    hashlib.sha1)

    return hash.hexdigest()

class SimpleObject(object):
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return self.name

#写入端
out_s = StringIO()

o = SimpleObject("match")
pickled_data = pickle.dumps(o)
digest = make_digest(pickled_data)
header = "%s %s"%(digest,len(pickled_data))
print "WRITING:",header
out_s.write(header + '\n')
out_s.write(pickled_data)

o = SimpleObject("dismatch")
pickled_data = pickle.dumps(o)
digest = make_digest("Ohter Data")
header = "%s %s"%(digest,len(pickled_data))
print "\nWRITING:",header
out_s.write(header + '\n')
out_s.write(pickled_data)

out_s.flush()

# 读取端
in_s = StringIO(out_s.getvalue())
while True:
    first_line = in_s.readline()
    if not first_line:
        break
    incoming_digest, incoming_length = first_line.split(' ') 
    print '\nRead:',incoming_digest,incoming_length.strip()

    incoming_length = int(incoming_length)
    incoming_pickled_data = in_s.read(incoming_length)
    actual_digest = make_digest(incoming_pickled_data)
    print "Autual:",actual_digest

    if actual_digest != incoming_digest:
        print "WARNING: Data corruption"
    else:
        obj = pickle.loads(incoming_pickled_data)
        print "OK:",obj



    








