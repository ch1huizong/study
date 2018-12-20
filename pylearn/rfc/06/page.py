#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 验证闭包在惰性求值时的作用
try:
    from urllib import urlopen
except:
    from urllib.request import urlopen

def page(url):
    def get():
        return urlopen(url).read()
    return get
