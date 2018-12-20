#!/usr/bin/env python

from urlparse import urlparse, urlunparse

original = 'http://netloc/path;?#'
print'ORIG  :',original

parsed = urlparse(original)
print'PARSED:',type(parsed), parsed

t = parsed[:]
print'TUPLE :',type(t),t
print'NEW   :',urlunparse(t)
