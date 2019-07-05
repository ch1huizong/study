#!/usr/bin/env python

import urllib

query_args = {'q':'python funny','foo':'bar'}
encoded_args = urllib.urlencode(query_args)
print'Encoded:',encoded_args

url = 'http://localhost:8000/?' + encoded_args
print urllib.urlopen(url).read()
