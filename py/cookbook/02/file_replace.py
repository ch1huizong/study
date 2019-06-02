#! /usr/bin/env python
# -*- coding:UTF-8

import os
import sys

args = len(sys.argv)

if not  3 <= args <= 5:
    print "Usage: %s search_text replace_text [ infile [ outfile ] ]" % \
        os.path.basename(sys.argv[0])
else:
    stext = sys.argv[1]
    rtext = sys.argv[2]
    input_file = sys.stdin    # 默认了
    output_file = sys.stdout

    if args > 3:
        input_file = open(sys.argv[3])
    if args > 4:
        output_file = open(sys.argv[4],'w')

    for s in input_file:
        output_file.write(s.replace(stext,rtext))
    
    #output_file.write(input_file.read().replace(stext,rtext))  内存够大
    output_file.close()
    input_file.close()

