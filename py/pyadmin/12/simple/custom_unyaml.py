#! /usr/bin/env python3
# -*-coding:utf-8 -*-
# @Time    : 2019/06/19 17:02:12
# @Author  : che
# @Email   : ch1huizong@gmail.com

import yaml
import custom_class

yaml_file = open("custom_class.yaml", "r")
obj = yaml.load(yaml_file)
print(obj)
yaml_file.close()
