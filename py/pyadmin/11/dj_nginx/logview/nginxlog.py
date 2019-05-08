#!/usr/bin/env python 
# -*- coding:UTF-8 -*-
# nginxlog.py
#
# Parse an nginx log file into a sequence of dictionaries
import re

logpats  = r'(\S+) (\S+) (\S+) \[(.*?)\] ' \
           r'"(\S+) (\S+) (\S+)" (\S+) (\S+) '\
           r'"(\S+)" "(\S+)"'

logpat   = re.compile(logpats)

def field_map(dictseq, name, func):
    for d in dictseq:
        d[name] = func(d[name]) # 转化对应的列
        yield d

def nginx_log(lines):
    groups = (logpat.match(line) for line in lines)
    tuples = (g.groups() for g in groups if g)
    
    colnames = (
        'host','no1','no2','datetime',
        'method', 'request','proto','status',
        'bytes', 'referrer', 'user_agent'
    )

    log      = (dict(zip(colnames,t)) for t in tuples)
    log      = field_map(log,"status",int)
    log      = field_map(log,"bytes",
                         lambda s: int(s) if s != '-' else 0)
    return log
