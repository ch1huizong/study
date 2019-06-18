#! /usr/bin/env python3
# -*-coding:utf-8 -*-
# @Time    : 2019/06/18 10:52:41
# @Author  : che
# @Email   : ch1huizong@gmail.com

import sys


for i, line in enumerate(sys.stdin):
    print("%s: %s" % (i, line), end="")
