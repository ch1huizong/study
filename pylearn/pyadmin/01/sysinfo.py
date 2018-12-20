#! /usr/bin/env python
# -*- coding:UTF-8 -*-
# 系统信息收集

import subprocess

def uname_func():
    uname = "uname"
    uname_arg = "-a"
    print "Gathering system information with %s command:\n" % uname
    subprocess.call([uname, uname_arg])

def diskspace_func():
    diskspace = "df"
    diskspace_arg = "-h"
    print "Gathering system information with %s command:\n" % diskspace
    subprocess.call([diskspace, diskspace_arg])

def tmp_space():
    tmp_usage = "du"
    tmp_arg = "-h"
    path = "/tmp"
    print "Space used in /tmp directory"
    subprocess.call([tmp_usage, tmp_arg,path])

def main():
    print "-" * 69
    uname_func()
    print
    print "-" * 69
    diskspace_func()
    print
    print "-" * 69
    tmp_space()

if __name__ == '__main__':
    main()
