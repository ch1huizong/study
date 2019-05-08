#!/usr/bin/env python
# -*- coding:UTF-8 -*-
import dircache
import os

path='/tmp'
file_to_create=os.path.join(path,'pymtw_tmp.txt')

first=dircache.listdir(path)

#Create the new file
open(file_to_create,'wt').close()

# 重新扫描目录
second=dircache.listdir(path)

#Remove the file we created
os.unlink(file_to_create)


print'Identical :',first is second
print'Equal     :',first == second
print'Difference:',list(set(second)-set(first))
