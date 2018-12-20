#!/usr/bin/env python

from urlparse import urljoin

print urljoin('http://www.example.com/path/',
                '/subpath/file.html')

print urljoin('http://www.example.com/path/file.html',
                'subpath/file.html')

