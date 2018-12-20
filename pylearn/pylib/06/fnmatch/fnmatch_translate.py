#!/usr/bin/env python
# -*- coding:UTF-8 -*-

import fnmatch

pattern='fnmatch_*.py'
print'Pattern   :',pattern
print'Regex     :',fnmatch.translate(pattern)
