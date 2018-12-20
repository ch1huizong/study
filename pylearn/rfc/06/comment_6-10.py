#! /usr/bin/env python
# -*- coding:UTF-8 -*-

# 原例确实有问题
f = open('tracing_6-5.py')
lines = (t.strip() for t in f if t.strip())
comments = (t for t in lines if t[0] == '#' )
for c in comments:
    print(c)
