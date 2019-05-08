#!/usr/bin/env python
# -*- coding:UTF-8 -*-
import time

# 生成器模型
def tail(f):
    f.seek(0,2)
    while True:
        line = f.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line

def grep(lines,searchtext):
    for line in lines:
        if searchtext in line:
            yield line


# 协程模型,JOB
def print_matches(matchtext):
    print"Looking for",matchtext
    while True:
        line = (yield)
        if matchtext in line:
            print line
                

if __name__ =='__main__':
    matchers = [
        print_matches('python'),
        print_matches('guido'),
        print_matches('jython'),	
    ]				

    # 开启协程,准备接受数据
    for m in matchers: 
        m.next()

    pylog = tail(open('/var/log/syslog'))
    for line in pylog:
        for m in matchers:
            m.send(line)
