#! /usr/bin/env python3
# -*-coding:utf-8 -*-
# @Time    : 2019/06/19 22:44:36
# @Author  : che
# @Email   : ch1huizong@gmail.com

import optparse
import configparser


def read_config(file="hello_config.ini"):
    parser = configparser.ConfigParser()
    parser.read(file)
    sections = parser.sections()
    for section in sections:
        print(parser.items(section))
        return parser.items(section)[0][0]


def main():
    p = optparse.OptionParser()
    p.add_option("--sysadmin", "-s", dest="sysadmin", default="BOFH")
    p.add_option("--config", "-c", action="store_true")
    options, arguments = p.parse_args()

    if options.config:
        options.sysadmin = read_config()
    print("Hello, %s" % options.sysadmin)


if __name__ == "__main__":
    main()
