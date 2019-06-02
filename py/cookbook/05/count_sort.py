#!/usr/bin/env python
# -*- coding:UTF-8 -*-

#根据对应值将键或索引排序 


#将元素序列包装进字典，并提供统计结果
class hist(dict):    
	def add(self,item,increment=1):
		'''为item的条目增加计数'''
		self[item] = increment + self.get(item,0)
	
	def counts(self,reverse=False):
		'''返回根据对应值排序的键的列表'''
		aux = [ (self[k],k) for k in self]
		aux.sort()
		if reverse:
			aux.reverse()
		return [ key for val,key in aux ] # 键列表


# 列表储存统计结果,使用问题？
# 传入参数？
class histl(list):
	def __init__(self,n):
		'''初始化列表，统计n个不同项的出现'''
		list.__init__(self,n*[0])

	def add(self,item,increment=1):
		'''为item的条目增加计数'''
		self[item] += increment
	
	def counts(self,reverse=False):
		'''返回根据对应值排序的索引的列表'''
		aux = [ (v,k) for k,v in enumerate(self) ]
		aux.sort()
		if reverse:
			aux.reverse()
		return [ k for v, k in aux]  # 索引列表

	
#重构counts方法
def _sorted_keys(container,keys,reverse):
	'''返回keys的列表，根据container中的对应值排序'''
	aux = [ (container[key],key) for key in keys]
	aux.sort()
	if reverse: aux.reverse()
	return [ k for v,k in aux ]

def _sorted_keys_v2(container,keys,reverse):
	return sorted(keys, key=container.__getitem__,reverse=reverse)

def _dict_items_sorted_by_value(d, reverse=False):
	from operator import itemgetter   # 应用与子项是容器的序列
	return sorted(d.iteritems(), key=itemgetter(1),reverse=reverse)
	
#class hist(dict):
#	...
#	def counts(self,reverse=False):
#		return _sorted_keys(self,self,reverse)
#
#
# class histl(list):
#	...
#	def counts(self,reverse=False):
#		return _sorted_keys(self,xrange(len(self)),reverse)
#

if __name__ == '__main__':
    sentence = '''Hello there this is a test. Hello there this was a test,
                but now it is not. '''
    words = sentence.split()
    d = hist()
    for word in words: d.add(word)
    print "Ascending count:"
    print d.counts()
    print
    print "Descending count:"
    print d.counts(reverse=True)



