#! /usr/bin/env python
# -*- coding:UTF-8 -*-

import sys
print "Welcome."
print "Please enter a string:"
sys.stdout.flush()   # 必要,无缓冲
line = sys.stdin.readline().strip()
print "You entered %d characters." % len(line)
