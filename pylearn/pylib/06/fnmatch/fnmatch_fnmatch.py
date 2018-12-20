#!/usr/bin/env python
# -*- coding:UTF-8 -*-
import os
import fnmatch

pattern='fnmatch_*.py'
print'Pattern   :',pattern
print 

files=os.listdir('.')
for name in files:
    print'Filename: %-25s   %s'%\
        (name,fnmatch.fnmatch(name,pattern))
