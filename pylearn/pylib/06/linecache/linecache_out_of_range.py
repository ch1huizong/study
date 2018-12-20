#!/usr/bin/env python
# -*- coding:UTF-8 -*-
import linecache
from linecache_data import *

filename=make_tempfile()

#A line that not exists return a empty string
not_there=linecache.getline(filename,500)
print'NOT THERE:%r includes %d characters'%(not_there,len(not_there))

cleanup(filename)
