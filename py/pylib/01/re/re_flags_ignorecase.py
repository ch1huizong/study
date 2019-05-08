#!/usr/bin/env python
# -*- coding:UTF-8 -*-

import re

text = 'This is some text -- with punctuation.'
pattern = r'\bT\w+'
with_case = re.compile(pattern)
without_case = re.compile(pattern,re.IGNORECASE)

print'Text:\n %r' % text
print'Pattern:\n %s' % pattern

print'Case-sensitive:'
for match in with_case.findall(text):
    print'  %r' % match

print'Case-insensitive:'
for match in without_case.findall(text):
    print'  %r' % match

