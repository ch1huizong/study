#! /usr/bin/env python
# -*- coding:UTF-8 -*-

import zlib
import binascii

original_data = "This is the original text."

fmt = '%15s     %15s'
print fmt % ('len(data)', 'len(compressed)')
print fmt % ('-'*15, '-'*15)

for x in xrange(5):
    data = original_data * x
    compressed = zlib.compress(data)
    highlight = '*' if len(data) < len(compressed) else ''

    print fmt % (len(data),len(compressed)),highlight

