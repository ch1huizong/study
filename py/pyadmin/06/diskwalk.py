#! /usr/bin/env python3
# -*-coding:utf-8 -*-
# @Time    : 2019/06/15 16:44:35
# @Author  : che
# @Email   : ch1huizong@gmail.com

import os


class DiskWalk(object):
    def __init__(self, path):
        self.path = path

    def gen_paths(self):
        for dirpath, dirnames, filenames in os.walk(self.path):
            for file in filenames:
                fullpath = os.path.join(dirpath, file)
                yield fullpath

    def gen_files(self):
        for dirpath, dirnames, filenames in os.walk(self.path):
            for file in filenames:
                yield file

    def gen_dirs(self):
        for dirpath, dirnames, filenames in os.walk(self.path):
            for dir in dirnames:
                yield dir

    paths = property(gen_paths)
    files = property(gen_files)
    dirs = property(gen_dirs)
