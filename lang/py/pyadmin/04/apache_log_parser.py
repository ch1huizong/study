#! /usr/bin/env python3
# -*-coding:utf-8 -*-
# @Time    : 2019/06/18 11:47:14
# @Author  : che
# @Email   : ch1huizong@gmail.com

import sys
import re


def dictify_logline0(line):
    split_line = line.split()  # 仅仅以空白分割，比较脆弱
    return {
        "remote_host": split_line[0],
        "status": split_line[8],
        "bytes_sent": split_line[9],
    }


log_line_re = re.compile(
    r"""
    (?P<remote_host>\S+)  # IP
    \s+
    \S+ # logname
    \s+
    \S+ # user
    \s+
    \[[^\[\]]+\] # time
    \s+
    "[^"]+" # request line
    \s+
    (?P<status>\d+)
    \s+
    (?P<bytes_sent>-|\d+)
    \s*
    """,
    re.VERBOSE,
)


def dictify_logline(line):
    m = log_line_re.match(line)
    if m:
        groupdict = m.groupdict()
        if groupdict["bytes_sent"] == "-":
            groupdict["bytes_sent"] = 0
        return groupdict
    else:
        return {"remote": None, "status": None, "bytes_sent": 0}


def gen_log_report(logfile):
    report_dict = {}
    for line in logfile:
        line_dict = dictify_logline(line)
        print(line_dict)

        try:
            bytes_sent = int(line_dict["bytes_sent"])
        except ValueError:
            bytes_sent = 0
        report_dict.setdefault(line_dict["remote_host"], []).append(bytes_sent)
    return report_dict


if __name__ == "__main__":
    if not len(sys.argv) > 1:
        sys.exit(1)

    infile_name = sys.argv[1]
    try:
        infile = open(infile_name, "r")
    except IOError:
        print("You must specify a valid file to parse")
        sys.exit(1)

    log_report = gen_log_report(infile)
    print(log_report)
    infile.close()
