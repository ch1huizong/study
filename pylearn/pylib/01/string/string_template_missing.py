#!/usr/bin/env python
# -*- coding:UTF-8 -*-

import string

values = {'var':'foo'}

t = string.Template('$var is here but $missing is not provided')

try:
    print 'substitute() :',t.substitute(values)
except KeyError,err:
    print'ERROR:',str(err)

# 安全方法
print 'safe_substitute() :',t.safe_substitute(values)
