#!/usr/bin/env python
# -*- coding:UTF-8 -*-

import os
from shutil import copy

os.mkdir('example')
print'BEFORE:',os.listdir('example')
copy('shutil_copy.py','example')
print'AFTER:',os.listdir('example')
