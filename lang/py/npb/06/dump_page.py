#! /usr/bin/env python
# -*- coding:UTF-8 -*-

import sys
import urllib2

req = urllib2.Request(sys.argv[1])
fd = urllib2.urlopen(req)
while True:
    data = fd.read(1024)
    if not data:
        break
    sys.stdout.write(data)
