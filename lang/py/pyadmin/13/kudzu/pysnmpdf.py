#! /usr/bin/env python3
# -*-coding:utf-8 -*-
# @Time    : 2019/06/20 10:51:49
# @Author  : che
# @Email   : ch1huizong@gmail.com

import optparse
from subprocess import call


def main():
    p = optparse.OptionParser(
        description="Python wrapped snmpd command",
        prog="pysnmpdf",
        version="0.1a",
        usage="%prog machine",
    )
    p.add_option("-c", "--community", help="snmp community string")
    p.add_option("-V", "--Version", help="snmp version to use")
    p.set_defaults(community="public", Version="2c")
    options, arguments = p.parse_args()

    if len(arguments) == 1:
        machine = arguments[0]
        call(["snmpdf", "-c", options.community, "-v", options.Version, machine])
    else:
        p.print_help()


if __name__ == "__main__":
    main()
