#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# .或..相对路径转换为绝对路径

import os
import os.path

os.chdir('/etc/apt')

for path in ['.',
    '..',
    './one/two/three',
    '../one/two/three',
    ]:
    print '%17s :   "%s"'%(path,os.path.abspath(path))
