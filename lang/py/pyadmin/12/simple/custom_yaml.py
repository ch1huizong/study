#! /usr/bin/env python3
# -*-coding:utf-8 -*-
# @Time    : 2019/06/19 16:59:22
# @Author  : che
# @Email   : ch1huizong@gmail.com

import yaml
from custom_class import MyClass


my_obj = MyClass()
my_obj.add_item(1)
my_obj.add_item(2)
my_obj.add_item(3)

yaml_file = open("custom_class.yaml", "w")
yaml.dump(my_obj, yaml_file)
yaml_file.close()
