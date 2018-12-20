#!/usr/bin/env python
# -*- coding:UTF-8 -*-

import re

text ='abbaadfafagafagbbabadfff'
pattern = 'ab'

for match in re.findall(pattern,text):
    print'Found "%s"' % match

