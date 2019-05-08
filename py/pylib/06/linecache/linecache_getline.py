#!/usr/bin/env python
# -*- coding:UTF-8 -*-
import linecache
from linecache_data import *

filename=make_tempfile()

#Pick out the same line from source and cache
print'SOURCE:'
print'%r'%lorem.split('\n')[4]
print
print'CACHE:'
print'%r'%linecache.getline(filename,5)         #note!

cleanup(filename)
