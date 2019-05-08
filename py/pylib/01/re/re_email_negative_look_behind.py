#!/usr/bin/env python
# -*- coding:UTF-8 -*-

import re

address = re.compile('''
    
    ^

    #the address itself
    [\w\d.+-]+              #username

    #Ignore noreply addresses
    (?<!noreply)

    @
    ([\w\d.]+\.)+           #domain name prefix
    (com|org|edu)           # domain name
    

    $
    ''',
    re.UNICODE| re.VERBOSE)

candidates = [
    u'first.last@example.com',
    u'noreply@example.com',
    ]

for candidate in candidates:
    print'  Candidate:',candidate
    match = address.search(candidate)
    if match:
        print'  Match:',candidate[match.start():match.end()]
        print
    else:
        print'  No match'
        print
