#!/usr/bin/env python 
# -*- coding:UTF-8 -*-
#
# follow.py
# 
# Follow a file like tail -f.

# 无限数据流
import time
def follow(thefile):
    thefile.seek(0,2)
    try:
        while True:
            line = thefile.readline()
            if not line:
                time.sleep(0.1)
                continue
            yield line
    except GeneratorExit:   # 暗示follow会无限运行下去?
        print "Follow :shutting down."

# Example use
# Note : This example requires the use of an apache log simulator.
# 
# Go to the directory run/foo and run the program 'logsim.py' from
# that directory.   Run this program as a background process and
# leave it running in a separate window.  We'll write program
# that read the output file being generated
# 

if __name__ == '__main__':
    logfile = open("run/foo/access-log","r")
    loglines = follow(logfile)
    for line in loglines:
        print line,
