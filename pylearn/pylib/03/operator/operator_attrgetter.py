#!/usr/bin/env python

from operator import *

class MyObj(object):
	def __init__(self,arg):
		super(MyObj,self).__init__()
		self.arg = arg
	def __repr__(self):
		return"MyObj(%s)"%self.arg

l = [ MyObj(i) for i in xrange(5) ]
print'objects	:',l

#set an attribute getter
g = attrgetter('arg')
vals = [ g(i)  for i in l ]
print'arg values:',vals

l.reverse()
print'reversed	:',l
print'sorted	:',sorted(l,key=g)


