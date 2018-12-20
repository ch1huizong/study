#!/usr/bin/env python
# -*- coding:UTF-8 -*-

import re

twitter = re.compile(
    '''
    (?<=@)
    ([\w\d_]+)
    ''',
    re.UNICODE | re.VERBOSE)

text = '''
This text includes two twitter handles.
One for @ThePSF, and one for the author,@doughellmann.
'''
print text

for match in twitter.findall(text):
    print'Handle:',match
