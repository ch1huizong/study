#! /usr/bin/env python3
# -*-coding:utf-8 -*-
# @Time    : 2019/06/15 18:36:58
# @Author  : che
# @Email   : ch1huizong@gmail.com
# 寻找某一路径下的重复文件

from os.path import getsize

from checksum import create_checksum
from diskwalk import DiskWalk


def find_dupes(path='tmp'):
    dups = []
    record = {}

    d = DiskWalk(path)
    files = d.paths

    for file in files:
        compound_key = (getsize(file), create_checksum(file))
        if compound_key in record:
            dups.append(file)
        else:
            record[compound_key] = file
    return dups


if __name__ == '__main__':
    dups = find_dupes()
    for d in dups:
        print('Duplicate: %s' % d)
