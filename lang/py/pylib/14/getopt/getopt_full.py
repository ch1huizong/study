#! /usr/bin/env python
# -*- coding:UTF-8 -*-

import getopt
import sys

version = '1.0'
verbose = False
output_filename = 'default.out'


print 'ARGV    :',sys.argv[1:]
try:
    options, reminder = getopt.getopt(sys.argv[1:],'o:v',['output=','verbose','version='])
except getopt.GetoptError as e:
    print "ERROR:",e
    sys.exit(1)

print "OPTIONS    :",options

for opt,val in options:
    if opt in ['-o', '--output']:
        output_filename = val
    elif opt in ['v', '--verbose']:
        verbose = True
    elif opt == '--version':
        version = val

print 'VERSION    :',version
print 'VERBOSE    :',verbose
print 'OUTPUT    :', output_filename
print 'REMINDER    :',reminder


