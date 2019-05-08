#!/usr/bin/env python
# -*- coding:UTF-8 -*-

from shutil import *
from commands import *

print'BEFORE:'
print getoutput('ls -rlast /tmp/example')
rmtree('/tmp/example')
print'AFTER:'
print getoutput('ls -rlast /tmp/example')
