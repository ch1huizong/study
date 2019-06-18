#! /usr/bin/env python3
# -*-coding:utf-8 -*-
# @Time    : 2019/06/18 16:32:41
# @Author  : che
# @Email   : ch1huizong@gmail.com

import shelve
from apache_log_parser import dictify_logline


logfile = open("/var/log/apache2/access.log", "r")
shelve_file = shelve.open("access.s")

for line in logfile:
    dict_line = dictify_logline(line)
    shelve_file[dict_line["remote_host"]] = shelve_file.setdefault(
        dict_line["remote_host"], 0
    ) + int(dict_line["bytes_sent"])

logfile.close()
shelve_file.close()
