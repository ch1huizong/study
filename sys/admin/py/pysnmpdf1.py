#! /usr/bin/env python3
# -*-coding:utf-8 -*-
# @Time    : 2019/06/20 10:51:49
# @Author  : che
# @Email   : ch1huizong@gmail.com

import optparse
import subprocess
from subprocess import Popen
import re


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

        def parse():
            p = Popen(
                ["snmpdf", "-c", options.community, "-v", options.Version, machine],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            return p.stdout

        pattern = r"9[0-9]%"
        outline = (line.decode().strip().split() for line in parse())
        flags = (" ".join(row) for row in outline if re.search(pattern, row[-1]))
        for flag in flags:
            print("%s CRITICAL" % flag)

    else:
        p.print_help()


if __name__ == "__main__":
    main()
