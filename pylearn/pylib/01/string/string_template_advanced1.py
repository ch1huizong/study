#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# 更高级版本，使用了元类和正则
# 留给正则表达式

import string
import re

class MyTemplate(string.Template):
    delimiter = '{{'
    pattern = r'''
    \{\{(?:
    (?P<escaped>\{\{) |
    (?P<named>[_a-z][_a-z0-9]*)\}\}|
    (?P<braced>>[_a-z][_a-z0-9]*)\}\}|
    (?P<invalid>)
    )
    '''

t = MyTemplate('''
    {{{{
    {{var}}
    ''')

print 'MATCHES:',t.pattern.findall(t.template)
print 'SUBSTITUTED:', t.safe_substitute(var='replacement')

