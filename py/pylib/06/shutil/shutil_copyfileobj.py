#!/usr/bin/env python
# -*- coding:UTF-8 -*-

import os
from StringIO import StringIO
import sys

from shutil import copyfileobj

class VerboseStringIO(StringIO):
    def read(self,n=-1):
        next=StringIO.read(self,n)
        print'read(%d) bytes'%n
        return next

lorem_ipsum = '''Lorem ipsum dolor sit amet, consectetuer adipiscing
elit. Vestibulum aliquam mollis dolor. Donec vulputate nunc ut diam.
Ut rutrum mi vel sem. Vestibulum ante ipsum.'''

print'Default:'
input=VerboseStringIO(lorem_ipsum)
output=StringIO()
copyfileobj(input,output)  #默认copyfileobj块

print

print'All at once:'
input=VerboseStringIO(lorem_ipsum)
output=StringIO()
copyfileobj(input,output,-1) #全部读取

print

print'Blocks of 256:'
input=VerboseStringIO(lorem_ipsum)
output=StringIO()
copyfileobj(input,output,256) # 自定义块
