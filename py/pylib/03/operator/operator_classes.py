#!/usr/bin/env python

from operator import *

class MyObj(object):
	def __init__(self,val):
		super(MyObj,self).__init__()
		self.val = val
	def __str__(self):
		return"MyObj(%s)"%self.val

	def __lt__(self,other):
		print'Testing %s < %s'%(self,other)
		return self.val < other.val

	def __add__(self,other):
		print'Adding %s + %s'%(self,other)
		return MyObj(self.val + other.val)

a = MyObj(1)
b = MyObj(2)

print'Comparision:'
print lt(a,b)

print'\nArithmetic:'
print add(a,b)

