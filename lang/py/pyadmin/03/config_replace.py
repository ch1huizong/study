#! /usr/bin/env python3
# -*-coding:utf-8 -*-
# @Time    : 2019/06/17 22:34:08
# @Author  : che
# @Email   : ch1huizong@gmail.com
# 设置了一个状态机，可以作为解析一切配置文件的原型

from io import StringIO
import re
import sys

vhost_start = re.compile(r"<VirtualHost\s+(.*?)>")
vhost_end = re.compile(r"</VirtualHost")
docroot_re = re.compile(r"(DocumentRoot\s+)(\S+)")


def replace_docroot(conf_string, vhost, new_docroot):
    conf_file = StringIO(conf_string)
    in_vhost = False
    curr_vhost = None

    for line in conf_file:
        m = vhost_start.search(line)
        if m:
            curr_vhost = m.groups()[0]
            in_vhost = True
        if in_vhost and (curr_vhost == vhost):
            docroot_match = docroot_re.search(line)
            if docroot_match:
                subline = docroot_re.sub(r"\1%s" % new_docroot, line)
                line = subline
        vhost_end_match = vhost_end.search(line)
        if vhost_end_match:
            in_vhost = False
        yield line


if __name__ == "__main__":
    conf_file = sys.argv[1]
    vhost = sys.argv[2]
    docroot = sys.argv[3]
    conf_string = open(conf_file).read()
    for line in replace_docroot(conf_string, vhost, docroot):
        print(line, end="")
