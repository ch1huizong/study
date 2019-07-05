#!/usr/bin/env python
# -*- coding:UTF-8 -*-

import re

address = re.compile('[\w\d.+-]+@([\w\d.]+\.)+(com|org|edu)',re.UNICODE)

candidates = [
    u'first.last@example.com',
    u'first.last+category@gmail.com',
    u'valid-address@mail.example.com',
    u'not-valide@example.foo',
    ]

for candidate in candidates:
    match = address.search(candidate)
    print'%-30s %s'%(candidate,'Matches' if match else 'No match')
