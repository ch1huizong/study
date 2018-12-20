#! /usr/bin/env python
# -*- coding:UTF-8 -*-
# urllib的ftp客户端

"""
url retriever

Usage:
urllib_ftp.py  URL FILENAME

URL:
FTP URL

FILENAME:
Download file as
"""

import urllib
import sys

if '-h' in sys.argv or '--help' in sys.argv:
    print __doc__
    sys.exit(1)

if not len(sys.argv) == 3:
    print 'URL and FILENAME are mandatory'
    print __doc__
    sys.exit(1)

url = sys.argv[1]
filename = sys.argv[2]
urllib.urlretrieve(url, filename)
