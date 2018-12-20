#!/usr/bin/env python

import textwrap
from example import sample

print sample
print
print'No dedent:\n'
print textwrap.fill(sample,width=50)
