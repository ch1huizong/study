#!/usr/bin/env python
# -*- coding:UTF-8 -*-

import re

def test_patterns(text,patterns=[]):
    for pattern, desc in patterns:
        print'Pattern %r (%s)\n' % (pattern,desc)
        print'%r' % text
        for match in re.finditer(pattern,text):
            s = match.start()
            e = match.end()
            substr = text[s:e]
            n_backslashes = text[:s].count('\\')     #Why?统计，没啥具体用
            prefix = '.'*(s + n_backslashes)
            print'%s%r' % (prefix,substr)
        print
    return

if __name__ == '__main__':
    test_patterns('abbaaabbbbaaaaa',[('ab',"'a' followed by 'b'"),])
