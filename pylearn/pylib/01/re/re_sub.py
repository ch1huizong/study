#!/usr/bin/env python 
# -*- coding:UTF-8 -*-

# 修改字符串
import re

bold = re.compile(r'\*{2}(.*?)\*{2}')

text = 'Make this **bold**. This **too**.'

print'Text:',text
print'Bold:',bold.sub(r'<b>\1</b>',text) #引用了匹配分组
