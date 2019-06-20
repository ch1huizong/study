#!/usr/bin/env python
# -*- coding:UTF-8 -*-

"""快速排序"""

def qsort(L): # 使用列表推导
	if len(L) <= 1: return L
	return qsort([ lt for lt in L[1:] if lt < L[0]]) + L[0:1] +\
			qsort([ ge for ge in L[1:] if ge >= L[0] ] )	

def qsort_v2(L):  # 使用语句
	if not L: return L
	pivot = L[0]
	def lt(x): return x<pivot
	def ge(x): return x>=pivot
	return qsort(filter(lt,L[1:])) + [pivot] + qsort(filter(ge,L[1:]))

def qs_test(length):
	import random
	joe = range(length)
	random.shuffle(joe)
	qsJoe = qsort(joe)
	for i in range(len(qsJoe)):
		assert qsJoe[i] == i,'qsort is broken at %d!'%i

if __name__ == '__main__':
	qs_test(15)
