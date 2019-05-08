#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# 磁盘会写入

import mmap
import shutil
import contextlib

shutil.copyfile('lorem.txt','lorem_copy.txt')

word='consectetuer'
reversed1=word[::-1]
print'Looking for   :',word
print'Replaciing with:',reversed1

with open('lorem_copy.txt','r+') as f:
    with contextlib.closing(mmap.mmap(f.fileno(),0)) as m:
        print'Before:'
        print m.readline().rstrip()
        m.seek(0)       #rewind

        loc=m.find(word)
        m[loc:loc+len(word)]=reversed1
        m.flush()  #如果不flush,一样有效

        m.seek(0)
        print'After:'
        print  m.readline().rstrip()

        f.seek(0)
        print'File  :'
        print f.readline().rstrip()

