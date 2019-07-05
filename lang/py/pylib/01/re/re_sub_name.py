#!/usr/bin/env python 
# -*- coding:UTF-8 -*-

import re

bold = re.compile(r'\*{2}(?P<bold_text>.*?)\*{2}',re.UNICODE)

text = 'Make this **bold**. This **too**.'

print'Text:',text
print'Bold:',bold.sub(r'<b>\g<bold_text></b>',text)
