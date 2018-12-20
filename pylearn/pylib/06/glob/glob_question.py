#!/usr/bin/env python
# -*- coding:UTF-8 -*-

import glob

for name in glob.glob('dir/file?.txt'):
    print name
