#!/usr/bin/env python
# -*- coding:UTF-8 -*-

from re_test_patterns import test_patterns

test_patterns('abbaabbba',
            [('[ab]','either a or b'),
            ('a[ab]+','a followed by 1 or more a or b'),
            ('a[ab]+?','not greedy') # 禁用贪心模式
            ])
