#! /usr/bin/env python
# -*- coding:UTF-8 -*-

import hashlib
from hashlib_data import lorem as data

h = hashlib.md5()
h.update(data)
all_at_once = h.hexdigest()

def chunk(size, text):
    start = 0
    while start < len(text):
        block = text[start:start+size]
        yield  block
        start += size

h = hashlib.md5()
for b in chunk(60,data):
    h.update(b)
line_by_line = h.hexdigest()

print "all_at_once:",all_at_once
print "line_by_line:",line_by_line
print "Same:",all_at_once == line_by_line



