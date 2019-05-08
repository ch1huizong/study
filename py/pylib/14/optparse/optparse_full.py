#! /usr/bin/env python
# -*- coding:UTF-8 -*-

import optparse
import sys

print 'ARGV    :',sys.argv[1:]
print

parser = optparse.OptionParser()
parser.add_option('-o','--output',dest='output_file',default='default.out')
parser.add_option('-v','--verbose',dest='verbose',action='store_true',default=False)
parser.add_option('--version',dest='version',type='float',default=1.0)
options, reminder = parser.parse_args()


print 'VERSION    :',options.version
print 'VERBOSE    :',options.verbose
print 'OUTPUT    :', options.output_file
print 'REMINDER    :',reminder


