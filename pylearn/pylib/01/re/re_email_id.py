#!/usr/bin/env python
# -*- coding:UTF-8 -*-

# 条件语句，动态改变模式
import re

address = re.compile('''
    ^

   (?P<name>
    ([\w.]+\s+)*[\w.]+ 
    )?  
    \s*

    #Eamil address are wrapped in angle brackets,but only if a name is found
    (?(name)                            # 1.step,如果name组匹配
        (?P<brackets>(?=(<.*>$)))       # 则建立bracket组，后面必须有<>
        |
        (?=([^<].*[^>]$))               # 若name组不匹配
    )

    (?(brackets)<|\s*)                  #2.step,若有bracket组或没有

    #the address itself
    (?P<email>
    [\w\d.+-]+              #username
    @
    ([\w\d.]+\.)+           #domain name prefix
    (com|org|edu)           # domain name
    )
    
    (?(brackets)>|\s*)                  #3.step

    $
    ''',
    re.UNICODE| re.VERBOSE)

candidates = [
    u'First Last <first.last@example.com>',
    u'No Brackets first.last@example.com',
    u'Open Bracket <first.last@example.com',
    u'Close Bracket first.last@example.com>',
    u'no.brackets@example.com>',
    ]

for candidate in candidates:
    print ' Candidate:',candidate
    match = address.search(candidate)
    if match:
        print'  Name:',match.groupdict()['name']
        print'  Email:',match.groupdict()['email']
    else:
        print'  No match'
    print
