#!/usr/bin/env python
# -*- coding:UTF-8 -*-

from shutil import *
from commands import *
import os

with open('file_to_change.txt','wt') as f:
    f.write('content')
os.chmod('file_to_change.txt',0444)

print'BEFORE:'
print getstatus('file_to_change.txt')
copymode('shutil_copymode.py','file_to_change.txt')
print'AFTER:'
print getstatus('file_to_change.txt')

