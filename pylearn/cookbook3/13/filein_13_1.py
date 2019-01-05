#! /usr/bin/env python3
# -*-coding:UTF-8 -*-
# @Time    : 2019/01/04 15:51:56
# @Author  : che
# @Email   : ch1huizong@gmail.com

import fileinput


with fileinput.input() as f_input:
    for line in f_input:
        print(line, end='')
