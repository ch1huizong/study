#!/usr/bin/env python
# -*- coding:UTF-8 -*-

import re

text = 'This is some text -- with punctuation.\nA second line.'
pattern = r'.+'
no_newlines = re.compile(pattern)
dotall = re.compile(pattern,re.DOTALL)

print'Text:\n %r' % text
print'Pattern:\n %s' % pattern

print'No newlines:'
for match in no_newlines.findall(text):
    print'  %r' % (match,)
print'Dotall:   '
for match in dotall.findall(text):
    print'  %r' % (match,)

