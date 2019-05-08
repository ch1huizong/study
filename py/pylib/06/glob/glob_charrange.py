#!/usr/bin/env python
# -*- coding:UTF-8 -*-

import glob
for name in glob.glob('dir/*[0-9].*'):
    print name
