#!/usr/bin/env python
# -*- coding:UTF-8 -*-

import re

text = 'This is some text -- with punctuation.'
print text
print

patterns = [
    (r'^(?P<first_word>\w+)','word at start of string'),
    (r'(?P<last_word>\w+)\S*$','word at end with punctuation'),
    (r'(?P<t_word>\bt\w+)\W+(?P<other_word>\w+)','word starting with t,another word'),
    (r'(?P<ends_with_t>\w+t)\b','word ending with t'),
    ]

for pattern, desc in patterns:
    regex = re.compile(pattern)
    match = regex.search(text)
    print'Matching "%s"'%pattern
    print ' ',match.groups()
    print ' ',match.groupdict()
    print

