#!/usr/bin/env python
# -*- coding:UTF-8 -*-

import dircache

path='.'
first=dircache.listdir(path)
second=dircache.listdir(path)

print'Contents  :'
for name in first:
    print' ',name

print
print'Identical:',first is second
print'Equal    :',first == second
