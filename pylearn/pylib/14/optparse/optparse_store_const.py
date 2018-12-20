#! /usr/bin/env python
# -*- coding:UTF-8 -*-
# 存储不变量选项

import optparse

parser = optparse.OptionParser()
parser.add_option('--earth', action='store_const',
                  const='earth',dest='element',
                  default='earth',
                 )
parser.add_option('--air', action='store_const',
                  const='air',dest='element',
                  default='air',
                 )
parser.add_option('--water', action='store_const',
                  const='water',dest='element',
                  default='water',
                 )
parser.add_option('--fire', action='store_const',
                  const='fire',dest='element',
                  default='fire',
                 )

options, args = parser.parse_args()

print options.element
