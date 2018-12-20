#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# 规范化路径
import os.path

for path in ['one//two//three',
    'one/./two/./three',
    'one/../alt/two/three', #这里会如何处理？忽略了！
    ]:
    print'%-20s  :   %s'%(path,os.path.normpath(path))
