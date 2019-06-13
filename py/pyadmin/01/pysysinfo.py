#! /usr/bin/env python3
# -*-coding:UTF-8 -*-
# @Time    : 2019/06/13 14:29:14
# @Author  : che
# @Email   : ch1huizong@gmail.com
# 系统信息收集

import subprocess


def uname_func():
    uname = "uname"
    uname_arg = "-a"
    print("Gathering system information with %s command:\n" % uname)
    subprocess.call([uname, uname_arg])


def diskspace_func():
    diskspace = "df"
    diskspace_arg = "-h"
    print("Gathering system information with %s command:\n" % diskspace)
    subprocess.call([diskspace, diskspace_arg])


def main():
    uname_func()
    diskspace_func()


if __name__ == "__main__":
    main()
