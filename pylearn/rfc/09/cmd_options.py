#! /usr/bin/env python3
# -*-coding:UTF-8 -*-
# @Time    : 2019/01/29 16:15:50
# @Author  : che
# @Email   : ch1huizong@gmail.com

import optparse


p = optparse.OptionParser()


p.add_option('-o', action='store', dest='outfile')
p.add_option('--output', action='store', dest='outfile')

p.add_option('-d', action='store_true', dest='debug')
p.add_option('--debug', action='store_true', dest='debug')

p.set_defaults(debug=False)

opts, args = p.parse_args()

outfile = opts.outfile
debugmode = opts.debug

print(outfile, debugmode, args)
