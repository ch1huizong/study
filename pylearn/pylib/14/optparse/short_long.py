#! /usr/bin/env python
# -*- coding:UTF-8 -*-

import optparse

def short():
    parser = optparse.OptionParser()
    parser.add_option('-a',action='store_true',default=False)
    parser.add_option('-b',action='store',dest='b')
    parser.add_option('-c',action='store',dest='c',type='int')

    print parser.parse_args(['-a','-bname','-c','3'])

def long():
    parser = optparse.OptionParser()
    parser.add_option('--noarg',action='store_true',default=False)
    parser.add_option('--withname',action='store',dest='withname')
    parser.add_option('--withage',action='store',dest='withage',type='int')

    print parser.parse_args(['--noarg','--withname','che','--withage=18'])
    
def test():
    print "Short:"
    short()
    print
    print "*" * 60
    print
    long()

test()




