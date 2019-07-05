#!/usr/bin/env python
# -*- coding:UTF-8 -*-

# 去除缩进和fill连用
import textwrap
from example import sample

de_text = textwrap.dedent(sample).strip()
for width in [45,70]:
    print'%d Columns:\n'%width
    print textwrap.fill(de_text,width)
    print

