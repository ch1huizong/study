#!/usr/bin/env python 
# -*- coding:UTF-8 -*-
#
# largest.py
#
# 查找对最大文件的请求
# Find the largest file

from linesdir import *
from apachelog import *

lines = lines_from_dir("access-log*","www")
log = apache_log(lines)

print "%d %s" % max((r['bytes'],r['request'])
                    for r in log)
