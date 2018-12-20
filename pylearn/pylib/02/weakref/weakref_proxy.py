#!/usr/bin/env python

import weakref

class ExpensiveObject(object):
	def __init__(self,name):
		self.name = name
	def __del__(self):
		print'(Deleting %s)'%self

obj = ExpensiveObject('My Object')
rel = weakref.ref(obj)
proxy = weakref.proxy(obj)

print'Via obj:',obj.name
print'Via rel:',rel().name
print'Via proxy:',proxy.name

del obj
print'After,via rel:',rel().name
print'After,Via proxy:',proxy.name




