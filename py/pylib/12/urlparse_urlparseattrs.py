#!/usr/bin/env python

from urlparse import urlparse

url = 'http://netloc/path;param?query=arg#frag'
parsed = urlparse(url)
print'scheme    :',parsed.scheme
print'netloc    :',parsed.netloc
print'path      :',parsed.path
print'params    :',parsed.params
print'query     :',parsed.query
print'fragment  :',parsed.fragment
print'username  :',parsed.username
print'password  :',parsed.password
print'hostname  :',parsed.hostname,'(netloc in lowercase)'
print'port      :',parsed.port
