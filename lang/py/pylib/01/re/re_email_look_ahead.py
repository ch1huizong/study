#!/usr/bin/env python
# -*- coding:UTF-8 -*-

import re

address = re.compile('''
   ((?P<name>
    ([\w.,]+\s+)*[\w.,]+) 

    \s+
    
    )                      #name is no longer optional,名字必须

    #LookAhead,断言前项
    (?= (<.*>$)             #wrapped
        |
        ([^<].*[^>]$)       #not wrapped
    )
    
    <?                      #start_option
    #the address itself
    (?P<email>
    [\w\d.+-]+              #username
    @
    ([\w\d.]+\.)+           #domain name prefix
    (com|org|edu)           # domain name
    )
    >?                      #end_optional
    ''',
    re.UNICODE| re.VERBOSE)

candidates = [
    u'First Last <first.last@example.com>',
    u'No Brackets first.last@example.com',
    u'Open Bracket <first.last@example.com',
    u'Close Bracket first.last@example.com>',
    ]

for candidate in candidates:
    print'  Candidate:',candidate
    match = address.search(candidate)
    if match:
        print'  Name:',match.groupdict()['name']
        print'  Email:',match.groupdict()['email']
        print
    else:
        print'  No match'
