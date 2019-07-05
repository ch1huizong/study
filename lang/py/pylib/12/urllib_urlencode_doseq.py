#!/usr/bin/env python

import urllib

query_args = {'foo':['python funny','foo','bar']}

print'Single    :',urllib.urlencode(query_args)
print'Sequence    :',urllib.urlencode(query_args,doseq=True)
