#! /usr/bin/env python3
# -*-coding:utf-8 -*-
# @Time    : 2019/06/19 23:27:08
# @Author  : che
# @Email   : ch1huizong@gmail.com

import optparse
import os


def main():
    p = optparse.OptionParser(
        description="Lists contents of two directories",
        prog="pymultils",
        version="0.1a",
        usage="%prog [--dir dir1 dir2]",
    )
    p.add_option("--dir", action="store", dest="dir", nargs=2)
    options, arguments = p.parse_args()
    if options.dir:
        for d in options.dir:
            print("Listing of %s:\n" % d)
            for filename in os.listdir(d):
                print(filename)
    else:
        p.print_help()


if __name__ == "__main__":
    main()
