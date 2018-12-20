#!/usr/bin/env python
# -*- coding:UTF-8 -*-

from shutil import *
from glob import glob

with open('example.txt','wt') as f:
    f.write('contents')

print'BEFORE:',glob('example*')
move('example.txt','example.out')
print'AFTER:',glob('example*')
