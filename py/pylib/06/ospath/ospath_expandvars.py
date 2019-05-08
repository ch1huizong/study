#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# 扩展环境变量

import os.path
import os

os.environ['MYVAR']='VALUE'

print os.path.expandvars('/path/to/$MYVAR')
