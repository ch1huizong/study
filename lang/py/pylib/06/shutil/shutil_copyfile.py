#!/usr/bin/env python
# -*- coding:UTF-8 -*-

from shutil import *
from glob import glob

print'BEFORE:',glob('shutil_copyfile.*')
copyfile('shutil_copyfile.py','shutil_copyfile.py.copy')
print'AFTER:',glob('shutil_copyfile.*')
