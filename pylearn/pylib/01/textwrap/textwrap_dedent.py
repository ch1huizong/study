#!/usr/bin/env python
# -*- coding:UTF-8 -*-

# 去除缩进
import textwrap
from example import sample

print sample
print
print'Dedent:\n'
print textwrap.dedent(sample).strip()
