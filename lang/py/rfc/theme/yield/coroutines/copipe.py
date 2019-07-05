#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# 
# copipe.py
#
# A simple example showing how to hook up a pipeline with
# coroutines.   To run this, you will need a log file.
# Run the program logsim.py in the background to get a data
# source.

from coroutine import coroutine

# A data source.  This is not a coroutine, but it sends
# data into one (target)

import time
def follow(thefile, target):
    thefile.seek(0,2)      # Go to the end of the file
    while True:
         line = thefile.readline()
         if not line:
             time.sleep(0.1)    # Sleep briefly
             continue
         target.send(line)


# A filter.
@coroutine
def grep(pattern,target):      # 接收输入并输出
    while True:
        line = (yield)           # Receive a line
        if pattern in line:
            target.send(line)    # Send to next stage

# A sink.  A coroutine that receives data

@coroutine
def printer():
    while True:
         line = (yield)
         print line,

# Example use
if __name__ == '__main__':  # 增加了中间处理的阶段
    f = open("access-log")
    follow(f,
           grep('python',
           printer()))
