#! /usr/bin/env python3
# -*-coding:UTF-8 -*-
# @Time    : 2019/06/13 14:59:39
# @Author  : che
# @Email   : ch1huizong@gmail.com

from pysysinfo import diskspace_func

import subprocess


def tmp_space():
    tmp_usage = "du"
    tmp_arg = "-h"
    path = "/tmp"
    print("Space used in /tmp directory")
    subprocess.call([tmp_usage, tmp_arg, path])


def main():
    diskspace_func()
    tmp_space()


if __name__ == "__main__":
    main()
