#!/usr/bin/env python
# -*- coding:UTF-8 -*-

from re_test_patterns import test_patterns

test_patterns(
            'abbaaabbbbaaaaa',
            [('a(ab)','a followed by ab'),
            ('a(a*b*)','a followed by n a and n b'),
            ('a(ab)*','a followed by 0-n ab'),
            ('a(ab)+','a followed by 1-n ab'),
            ])

