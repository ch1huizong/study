#! /usr/bin/env python3
# -*-coding:utf-8 -*-
# @Time    : 2019/06/19 22:52:43
# @Author  : che
# @Email   : ch1huizong@gmail.com

import optparse
import os


def main():
    p = optparse.OptionParser(
        description="Python 'ls' command clone",
        prog="pyls",
        version="0.1a",
        usage="%prog [directory]",
    )
    options, arguments = p.parse_args()
    if len(arguments) == 1:
        path = arguments[0]
        for filename in os.listdir(path):
            print(filename)
    else:
        p.print_help()


if __name__ == "__main__":
    main()
