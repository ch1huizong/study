#! /usr/bin/env python
# -*- coding:UTF-8 -*-

import subprocess

def multi(*args):
    for cmd in args:
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        out = p.stdout.read()
        print out


multi("df -h", "ls -l /tmp", "tail /var/log/syslog")
