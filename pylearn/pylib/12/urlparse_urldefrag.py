#!/usr/bin/env python

from urlparse import urldefrag

original = 'http://netloc/path;param?query=arg#frag'
print'original:',original
url, fragment = urldefrag(original)
print'url   :',url
print'fragment  :',fragment
