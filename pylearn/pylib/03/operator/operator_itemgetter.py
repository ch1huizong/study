#!/usr/bin/env python

from operator import *

l = [ dict(val=-1*i) for i in xrange(4) ]
print'Dictionaries:',l
g = itemgetter('val')
vals = [ g(i) for i in l]
print'	values:',vals
print'	sorted:',sorted(l,key=g)
print

l = [ (i,i*-2) for i in xrange(4) ]
print'Tuples	:',l
g = itemgetter(1)
vals = [ g(i)  for i in l ]
print'	values:',vals
print'	sorted:',sorted(l,key=g)


