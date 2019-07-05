#! /usr/bin/env python3
# -*-coding:utf-8 -*-
# @Time    : 2019/06/19 16:59:22
# @Author  : che
# @Email   : ch1huizong@gmail.com

import pickle
from custom_class import MyClass


my_obj = MyClass()
my_obj.add_item(1)
my_obj.add_item(2)
my_obj.add_item(3)

p_file = open("custom_class.pkl", "wb")
pickle.dump(my_obj, p_file)
p_file.close()
