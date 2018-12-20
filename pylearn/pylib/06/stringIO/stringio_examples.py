#!/usr/bin/env python
# -*- coding:UTF-8 -*-

try:
    from cStringIO import StringIO
except:
    from StringIO import StringIO

#write to a buffer
output=StringIO()
output.write('This goes into the buffer.\n')
print >>output,'And so does this.'

#retrieve the value written
print output.getvalue()
output.close()

#Initialize a read buffer
input1=StringIO('Initial value for read buffer')
print input1.read()
