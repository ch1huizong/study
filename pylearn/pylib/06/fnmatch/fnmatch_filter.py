#!/usr/bin/env python
# -*- coding:UTF-8 -*-

import fnmatch
import os
import pprint

pattern='fnmatch_*.py'
print'Pattern    :',pattern

files=os.listdir('.')

print
print'Files     :'
pprint.pprint(files)

print
print'Matches   :'
pprint.pprint(fnmatch.filter(files,pattern))

