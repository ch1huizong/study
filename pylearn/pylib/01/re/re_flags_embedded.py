#!/usr/bin/env python
# -*- coding:UTF-8 -*-

import re

text = 'This is some text -- with punctuation.'
pattern = r'(?i)\bT\w+'  # 模式表达式中加入标志
regex = re.compile(pattern)

print'Text  :',text
print'Pattern   :',pattern
print'Matches   :',regex.findall(text)

