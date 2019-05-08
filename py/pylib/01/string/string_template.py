#!/usr/bin/env python
# -*- coding:UTF-8 -*-

import string

values = {'var':'foo'}

# 使用模板
t = string.Template("""
Variable    :$var
Escape      :$$
Variable in text    :${var}iable
""")

print'TEMPLATE:',t.substitute(values)

# 不使用模板
s= """
Variable    :%(var)s
Escape      :%%
Variable in text    :%(var)siable
"""

print'INTERPOLATION', s % values
