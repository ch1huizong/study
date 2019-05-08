#!/usr/bin/env python
# -*- coding:UTF-8 -*-

from re_test_patterns import test_patterns

test_patterns(
    'This is some text -- with punctuation.',
    [('[^-. ]+','sequences without -,.,or space')])
