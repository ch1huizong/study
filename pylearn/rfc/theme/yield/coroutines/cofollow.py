#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#
# cofollow.py
#
# A simple example showing how to hook up a pipeline with
# coroutines.   To run this, you will need a log file.
# Run the program logsim.py in the background to get a data
# source.

from coroutine import coroutine

# A data source.  This is not a coroutine, but it sends
# data into one (target)

import time
def follow(thefile, target): # 源
    thefile.seek(0,2)      # Go to the end of the file
    while True:
         line = thefile.readline()
         if not line:
             time.sleep(0.1)    # Sleep briefly
             continue
         target.send(line)

# A sink.  A coroutine that receives data
@coroutine
def printer(): # 端
    while True:
         line = (yield)
         print line,

# Example use
if __name__ == '__main__':
    f = open("access-log")
    follow(f, printer())
