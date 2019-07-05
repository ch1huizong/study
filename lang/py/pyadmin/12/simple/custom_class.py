#! /usr/bin/env python3
# -*-coding:utf-8 -*-
# @Time    : 2019/06/19 16:56:57
# @Author  : che
# @Email   : ch1huizong@gmail.com


class MyClass(object):
    def __init__(self):
        self.data = []

    def __str__(self):
        return "Custom Class MyClass Data:: %s" % str(self.data)

    def add_item(self, item):
        self.data.append(item)
