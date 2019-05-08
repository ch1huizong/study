#!/usr/bin/env python
# -*- coding:UTF-8 -*-

import re

address = re.compile('''
   ((?P<name>
    ([\w.,]+\s+)*[\w.,]+) 
    \s*
    <                       # < 和名字同时出现
    )?                      #the entire name is optional 

    #the address itself
    (?P<email>
    [\w\d.+-]+              #username
    @
    ([\w\d.]+\.)+           #domain name prefix
    (com|org|edu)           # domain name
    )
    >?                      #optional
    ''',
    re.UNICODE| re.VERBOSE)

candidates = [
    u'first.last@example.com',
    u'first.last+category@gmail.com',
    u'valid-address@mail.example.com',
    u'not-valide@example.foo',
    u'First Last <first.last@example.com>',
    u'No Brackets first.last@example.com',
    u'First Last',
    u'Frist Middle Last <first.last@example.com>',
    u'Frist M. Last <first.last@example.com>',
    u'<first.last@example.com>',
    ]

for candidate in candidates:
    print 'Candidate:',candidate
    match = address.search(candidate)
    if match:
        print'  Name:',match.groupdict()['name']
        print'  Email:',match.groupdict()['email']
    else:
        print'  No match'
    print 
