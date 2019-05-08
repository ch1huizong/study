#! /usr/bin/env python
# -*- coding:UTF-8 -*-

import optparse

parser = optparse.OptionParser()
parser.add_option('-c',type='choice',choices=['a','b','c'])

options, args = parser.parse_args()

print 'Choice:',options.c


