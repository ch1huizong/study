#!/usr/bin/env python
# -*- coding:UTF-8 -*-

import re

address = re.compile('''
    [\w\d.+-]+              #username
    @
    ([\w\d.]+\.)+           #domain name prefix
    (com|org|edu)           # domain name
    ''',
    re.UNICODE| re.VERBOSE)

candidates = [
    u'first.last@example.com',
    u'first.last+category@gmail.com',
    u'valid-address@mail.example.com',
    u'not-valide@example.foo',
    ]

for candidate in candidates:
    match = address.search(candidate)
    print'%-30s %s' % (candidate,'Matches' if match else 'No match')
