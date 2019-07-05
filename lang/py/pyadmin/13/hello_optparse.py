#! /usr/bin/env python3
# -*-coding:utf-8 -*-
# @Time    : 2019/06/19 22:44:36
# @Author  : che
# @Email   : ch1huizong@gmail.com

import optparse


def main():
    p = optparse.OptionParser()
    p.add_option("--sysadmin", "-s", dest="sysadmin", default="BOFH")
    options, arguments = p.parse_args()
    print("Hello, %s" % options.sysadmin)


if __name__ == "__main__":
    main()
