#!/usr/bin/env python 
# -*- coding:UTF-8 -*-
#
# largefiles.py
#
# 查看大文件
# Find all transfers over a megabyte

from linesdir import *
from apachelog import *

lines = lines_from_dir("access-log*","www")
log = apache_log(lines)

large = (r for r in log
         if r['bytes'] > 1000000)

for r in large:
    print r['request'],r['bytes']


