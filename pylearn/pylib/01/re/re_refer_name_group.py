#!/usr/bin/env python
# -*- coding:UTF-8 -*-

# 引用命名元组
import re

address = re.compile(
    r'''

    #the regular name
    (?P<first_name>\w+)           #first name
    \s+
    (([\w.]+)\s+)?  #optional middle name
    (?P<last_name>\w+)           #last name
    
    \s+
    
    <

    #The address:first_name.last_name@domain.tld
    (?P<email>
        (?P=first_name)         #first name,引用命名组
        \.
        (?P=last_name)          #last name,引用命名组
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

