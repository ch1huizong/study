#!/usr/bin/env python
# -*- coding:UTF-8 -*-

from shutil import *
from commands import *

print'BEFORE:'
print getoutput('ls -rlast /tmp/example')
copytree('../shutil','/tmp/example')
print'\nAFTER:'
print getoutput('ls -rlast /tmp/example')
