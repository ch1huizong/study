#! /usr/bin/env python
# -*- coding:UTF-8 -*-

import subprocess

p = subprocess.Popen("tr a-z A-Z", shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
output, error = p.communicate("translate to upper")
print output
