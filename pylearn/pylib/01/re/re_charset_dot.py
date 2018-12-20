#!/usr/bin/env python
# -*- coding:UTF-8 -*-

from re_test_patterns import test_patterns

test_patterns('abbaabbba',
            [('a.',' a followed by any one char'),
             ('b.',' b followed by any one char'),
             ('a.*b','a followed by anything,ending in b'),
             ('a.*?b','a followed by anything ,ending in b'),
            ])
