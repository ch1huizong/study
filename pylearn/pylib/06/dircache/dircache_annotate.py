#!/usr/bin/env python
# -*- coding:UTF-8 -*-

import dircache
from pprint import pprint
import os

path='../..'

contents=dircache.listdir(path)

annotated=contents[:]
dircache.annotate(path,annotated)

fmt='%25s\t%25s'

print fmt % ('ORIGINAL','ANNOTATED')
print fmt % (('-'*25,)*2)

for o,a in zip(contents,annotated):
    print fmt % (o,a)

