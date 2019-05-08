#!/usr/bin/env python
# -*- coding:UTF-8 -*-

import re

text = 'This is some text -- with punctuation.'
print'Input text        :',text

regex = re.compile(r'(\bt\w+)\W+(\w+)')
print'Pattern           :',regex.pattern

match = regex.search(text)
print'Entire match  :',match.group(0)
print'Word starting with "t":',match.group(1)
print'Word after "t" word :',match.group(2)

