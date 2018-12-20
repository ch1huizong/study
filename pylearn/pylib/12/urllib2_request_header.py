#!/usr/bin/env python

import urllib2

request = urllib2.Request('http://localhost:8080/')
request.add_header(
    'User-agent',
    'MOZilla')

response = urllib2.urlopen(request)
data = response.read()
print data
