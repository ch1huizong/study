#!/usr/bin/env python
# -*- coding:UTF-8 -*-

import re

address = re.compile(
    r'''

    #the regular name
    (\w+)           #first name
    \s+
    (([\w.]+)\s+)?  #optional middle name
    (\w+)           #last name
    
    \s+
    
    <

    #The address:first_name.last_name@domain.tld
    (?P<email>
        \1          #first name
        \.
        \4          #last name
        @
        ([\w\d.]+\.)+   #domain name
        (com|org|edu)
    )
    >
    ''',
    re.UNICODE | re.VERBOSE | re.IGNORECASE)

candidates = [
    u'First Last <first.last@example.com>',
    u'Different Name<first.last@example.com>',
    u'First Middle Last <first.last@example.com>',
    u'First M. Last <first.last@example.com>',
  ]
    
for candidate in candidates:
    print'Candidate:',candidate
    match = address.search(candidate)
    if match:
        print'  Match name:',match.group(1),match.group(4)
        print'  Match email:',match.group(5)
    else:
        print'  No match'
    print

