#!/usr/bin/env python
# -*- coding:UTF-8 -*-

from re_test_patterns import test_patterns

# 禁用贪心模式
test_patterns(
    'abbaabbba',
    [('ab*?','>=0'),
     ('ab+?','>=1'),
     ('ab??','0 <= num <=1'),
     ('ab{3}?','three times'),
     ('ab{2,3}?','two to three'),
    ])
