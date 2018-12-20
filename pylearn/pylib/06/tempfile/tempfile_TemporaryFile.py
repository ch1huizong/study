#!/usr/bin/env python

import os
import tempfile

print'Building a filename with PID:'
filename='/tmp/guess_my_name.%s.txt'%os.getpid()
temp=open(filename,'w+b')
try:
    print'temp:'
    print'  ',temp
    print'temp.name:'
    print'  ',temp.name
finally:
    temp.close()
    os.remove(filename)

print
print'TemporaryFile:'
temp=tempfile.TemporaryFile()
try:
    print'temp:'
    print'  ',temp
    print'temp.name'
    print'  ',temp.name
finally:
    temp.close()
