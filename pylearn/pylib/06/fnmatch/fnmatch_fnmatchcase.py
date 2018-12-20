#!/usr/bin/env python
# -*- coding:UTF-8 -*-
import os
import fnmatch

pattern='FNMATCH_*.PY' 
print'Pattern   :',pattern
print

files=os.listdir('.')
for name in files:
    print'Filename: %-25s   %s'%\
        (name,fnmatch.fnmatchcase(name,pattern))
