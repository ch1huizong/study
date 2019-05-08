#!/usr/bin/env python

from urlparse import urljoin

print urljoin('http://www.example.com/path/file.html',
                'anotherfile.html')

print urljoin('http://www.example.com/path/file.html',
                '../anotherfile.html')

