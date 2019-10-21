#! /usr/bin/env python3
# -*-coding:utf-8 -*-
# @Time    : 2019/06/26 10:31:11
# @Author  : che
# @Email   : ch1huizong@gmail.com
# 可以删除特定目录下的所有重复文件,NB


import os
import hashlib
from os.path import getsize


class DiskWalk(object):
    """遍历特定路径 产生文件，目录，绝对文件路径 """

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


def create_checksum(path):
    """产生文件的md5码"""

    with open(path, "rb") as fp:
        checksum = hashlib.md5()
        while True:
            buff = fp.read(8192)
            if not buff:
                break
            checksum.update(buff)
        checksum = checksum.digest()
        return checksum


def find_dupes(path):
    """寻找某一路径下的重复文件"""

    dups = []
    record = {}

    d = DiskWalk(path)
    files = d.paths

    for file in files:
        try:
            compound_key = (getsize(file), create_checksum(file))
        except Exception as e:
            continue

        if compound_key in record:
            dups.append(file)
        else:
            record[compound_key] = file
    return dups


class Delete(object):
    """文件删除模块"""

    def __init__(self, file):
        self.file = file

    def interactive(self):
        choice = input("Do you really want to delete %s [N]/Y? " % self.file)
        if choice.upper():
            print("DELETING: %s" % self.file)
            status = os.remove(self.file)
        else:
            print("Skipping: %s" % self.file)

    def dryrun(self):
        print("Dry Run: %s [NOT DELETED]" % self.file)

    def delete(self):
        print("DELETING: %s" % self.file)
        try:
            status = os.remove(self.file)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    dupes = find_dupes("/tmp")

    for d in dupes:
        delete = Delete(d)
        # delete.dryrun()
        # delete.interactive()
        delete.delete()
