#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# 扩展用户名, 需要加上'/',好像不是安全的

import os.path

for user in ['','dhellman','postgresql','/python','/self','/Public']:
    lookup='~'+ user
    print'%12s  :   %s'% (lookup,os.path.expanduser(lookup))
