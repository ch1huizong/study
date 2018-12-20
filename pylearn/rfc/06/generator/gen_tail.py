#! /usr/bin/env python3
# -*- coding:utf-8 -*-

""" python 版本tail -f | grep *
我们使用yield来构造一个工具模拟linux系统中的 "tail -f | grep *"行为 
""" 

import time


def tail(f): #获取监控文件最后一行
    f.seek(0,2)
    while True:    #连续不断产生行
        line = f.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line


def grep(lines, searchtext): # 搜寻包含特定文本的行
    for line in lines:
        if searchtext in line:
            yield line


if __name__ == '__main__':
    wwwlog = tail(open("/var/log/syslog"))
    pylines = grep(wwwlog, "python")
    for line in pylines:
        print(line, end='')
