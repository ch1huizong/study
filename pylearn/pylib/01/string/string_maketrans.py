#!/usr/bin/env python

import string

leet = string.maketrans('abegiloprstz','463611092572')
s = 'The quick brown fox jumped over the lazy dog.'

print s
print s.translate(leet)
