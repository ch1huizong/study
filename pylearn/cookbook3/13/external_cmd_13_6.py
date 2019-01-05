#! /usr/bin/env python3
# -*-coding:UTF-8 -*-
# @Time    : 2019/01/04 17:44:12
# @Author  : che
# @Email   : ch1huizong@gmail.com

import subprocess


text = b'''
hello world
this is a test
goodbye
'''

p = subprocess.Popen(['wc'], stdout=subprocess.PIPE, stdin=subprocess.PIPE)
stdout, stderr = p.communicate(text)

out = stdout.decode('utf-8')
print(out)
if stderr:
    err = stderr.decode('utf-8')
    print(err)
