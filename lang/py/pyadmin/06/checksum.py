#! /usr/bin/env python3
# -*-coding:utf-8 -*-
# @Time    : 2019/06/15 18:19:33
# @Author  : che
# @Email   : ch1huizong@gmail.com

import hashlib


def create_checksum(path):
    with open(path, 'rb') as fp:
        checksum = hashlib.md5()
        while True:
            buff = fp.read(8192)
            if not buff:
                break
            checksum.update(buff)
        checksum = checksum.digest()
        return checksum
