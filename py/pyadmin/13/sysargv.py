#! /usr/bin/env python3
# -*-coding:utf-8 -*-
# @Time    : 2019/06/19 22:37:55
# @Author  : che
# @Email   : ch1huizong@gmail.com

import sys

num_arguments = len(sys.argv) - 1

if num_arguments == 0:
    print("Hey, type in an option silly\n")
else:
    print(sys.argv, "You typed in ", num_arguments, "num_arguments")
