#! /usr/bin/env python3
# -*-coding:utf-8 -*-
# @Time    : 2019/06/15 16:44:35
# @Author  : che
# @Email   : ch1huizong@gmail.com

import os


class DiskWalk(object):
    def __init__(self, path):
        self.path = path

    @property
    def paths(self):
        for dirpath, dirnames, filenames in os.walk(self.path):
            for file in filenames:
                fullpath = os.path.join(dirpath, file)
                yield fullpath

    @property
    def files(self):
        for dirpath, dirnames, filenames in os.walk(self.path):
            for file in filenames:
                yield file

    @property
    def dirs(self):
        for dirpath, dirnames, filenames in os.walk(self.path):
            for dir in dirnames:
                yield dir
