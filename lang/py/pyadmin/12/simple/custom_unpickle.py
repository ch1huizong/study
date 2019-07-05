#! /usr/bin/env python3
# -*-coding:utf-8 -*-
# @Time    : 2019/06/19 17:02:12
# @Author  : che
# @Email   : ch1huizong@gmail.com

import pickle

up_file = open("custom_class.pkl", "rb")
obj = pickle.load(up_file)
print(obj)
up_file.close()
