#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# 若某个参数以os.sep开头，前面所有的参数都会舍去

import os.path

for parts in [ ('one','two','three'),
    ('/','one','two','three'),
    ('one','/two','three'),
    ]:
    print parts,' : ',os.path.join(*parts)
