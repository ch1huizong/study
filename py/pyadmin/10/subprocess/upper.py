#! /usr/bin/env python3
# -*-coding:utf-8 -*-
# @Time    : 2019/06/16 12:04:11
# @Author  : che
# @Email   : ch1huizong@gmail.com

import subprocess

p = subprocess.Popen(
    "tr a-z A-Z", shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE
)
output, error = p.communicate(b"translate to upper")
print(output)
