#!/usr/bin/env python
# -*- coding:UTF-8 -*-

import os.path

for path in ['/one/two/three',
    '/one/two/three/',
    '/',
    '.',
    '']:
    print'%15s  :   %s'%(path,os.path.basename(path))
