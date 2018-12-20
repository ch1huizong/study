#! /usr/bin/env python
# -*- coding:UTF-8 -*-

import os
import fnmatch

def gen_images(top, pattern):
    for path, dirs, files in os.walk(top):
        for f in files:
            if fnmatch.fnmatch(f, pattern):
                yield os.path.join(path, f)


for name in gen_images("/","*.jpg"):
    print name

