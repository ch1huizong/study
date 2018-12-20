#!/usr/bin/env python
# -*- coding:UTF-8 -*-

import mmap
import shutil
import contextlib

#Copy the example file
shutil.copyfile('lorem.txt','lorem_copy.txt')

word='consectetuer'
reversed1=word[::-1]

with open('lorem_copy.txt','r+') as f:
    with contextlib.closing(mmap.mmap(f.fileno(),0,access=mmap.ACCESS_COPY)) as m:
     
        print'Memory Before:'
        print m.readline().rstrip()
        
        print'File Before:'
        print f.readline().rstrip()
        print 
        
        m.seek(0)   #rewind
        loc=m.find(word)
        m[loc:loc+len(word)]=reversed1
        
        m.seek(0)
        print'Memory After:'
        print m.readline().rstrip()
        
        f.seek(0)
        print'File After    :'
        print f.readline().rstrip()
         
