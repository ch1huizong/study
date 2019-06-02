#!/usr/bin/env python

import sys, urllib

def reporthook(*a): print a
for url in sys.argv[1:]:
    i = url.rfind('/')
    files = url[i+1:]
    print url,'->',files
    urllib.urlretrieve(url,files,reporthook)
