#! /usr/bin/env python3
# -*-coding:utf-8 -*-
# @Time    : 2019/06/15 19:58:53
# @Author  : che
# @Email   : ch1huizong@gmail.com

import sys
from subprocess import call

source = "/tmp/dirA/"  # 注意末尾的/
target = "/tmp/dirB"

rsync = "rsync"
arguments = "-a"
cmd = "{rsync} {arguments} {source} {target}".format(
    rsync=rsync, arguments=arguments, source=source, target=target
)


def sync():
    ret = call(cmd, shell=True)
    if ret != 0:
        print("rsync failed")
        sys.exit(1)


sync()
