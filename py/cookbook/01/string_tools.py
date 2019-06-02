#!/usr/bin/env python
# -*- coding:UTF-8 -*-

from __future__ import division
import re
import itertools
import string
import sets
import struct

def isString_v1(obj):    #除了UserString
    return isinstance(obj,basestring)

def isString_v2(obj):    #鸭子方法
    try:
        obj + ''
    except:
        return False
    else:
        return True

def revwords_v1(astring):      #单词反转
    return  ' '.join(astring.split()[::-1])
    #return ' '.join(reversed(astring.split()))   # 紧凑

def revwords_v1(astring):      #单词反转，包括空白
    revwords = re.split(r'(\s+)',astring)
    revwords.reverse()
    revwords = ''.join(revwords)
    return revwords

def containsAny_v1(seq,aset):  #检查seq中是否拥有aset集合中的字符
    for c in seq:
        if c in aset: return True
    return False

def containsAny_v2(seq, aset):
    for item in itertools.ifilter(aset.__contains__,seq):
        return True
    return False

def containsAny_v3(seq,aset):   #集合交集
    return bool(set(aset).intersection(seq)) #会检查seq中所有元素

def contaisOnly(seq,aset):  # seq < aset, 检查seq中的所有字符是否都在集合aset中
    for c in seq:
        if c not in aset: return False
    return True

def containsAll(seq,aset):   # seq > aset,是否seq中包含aset所有项目
    return not set(aset).difference(seq)

# 特殊方法,需要两个参数都是字符集合，通用性不好
def containsAny_vs4(astring,astrset):
    notrans = string.maketrans('','')
    return len(astrset) != len(astrset.translate(notrans,astring))

def containsAll_vs1(astring,astrset):
    notrans = string.maketrans('','')
    return not astrset.translate(notrans,astring)
    
# 方法，需要特殊定制
def translator(frm='',to='',delete='',keep=None):
    if len(to) == 1:
        to = to * len(frm)  # 补齐
    
    trans = string.maketrans(frm,to)
    if keep is not None:
        allchars = string.maketrans('','')   # 256长度的字符串,所有字符
        delete = allchars.translate(allchars,\
                    keep.translate(allchars,delete)) # 移除的移除 
    def translate(s):                       # 闭包 
        return s.translate(trans,delete)
    return translate  # 返回一个特殊定制的函数

# 保留指定集合中的字符，过滤字符串
allchars = string.maketrans('','')
def makefilter(keep):
    delchars = allchars.translate(allchars,keep)  #补集

    def thefilter(s):    #闭包
        return s.translate(allchars,delchars)
    return thefilter    # 可以使用匿名函数lambda

def canonicform(s): # 使被保留字符串s以十分规整的形式返回
    return makefilter(s)(allchars)

# 过滤unicode字符串,基于它的translate
class Keeper(object):   # unicode形式的filter
    def __init__(self,keep):
        self.keep = sets.Set(map(ord,keep))
    def __getitem__(self,n):   # 如何与translate结合？     
        if n not in self.keep:
            return None
        return unichr(n)
    def __call__(self,s):
        return unicode(s).translate(self)  


text_chars = ''.join(map(chr,range(32,127)))+'\t\b\r\n' #文本字符集合
def isText(s,text_chars= text_chars,threshold=0.3):   #判断字符(节)串是文本还是二进制
    if '\0' in s:       #con1
        return False
    if not s:           # con2
        return True
    notext_chars = s.translate(all_chars,text_chars) 
    return len(notext_chars)/len(s) <= threshold  #con3

# 判断字符串是否capitalize
def iscapitalized(s):
    return s == s.capitalize() and containsAny_vs4(s,string.letters)  # 53

def fields(baseformat, theline, lastfield=False):
    """取得不固定长度的字段"""
    numremain = len(theline) - struct.calcsize(baseformat)
    formator = "%s %d%s" %(baseformat, numremain, lastfield and "s" or "x")
    return struct.unpack(formator, theline)

# 缓存版本
def fields_mem(baseformat, theline, lastfield=False, _cache={}):
    key = baseformat, theline, lastfield
    formator = _cache.get(key)
    if formator is None:
        numremain = len(theline) - struct.calcsize(baseformat)
        _cache[key]= formator = "%s %d%s" %(baseformat, numremain, lastfield and "s" or "x")
    return struct.unpack(formator, theline)


def split_by(theline, n ,lastfield=False):
    """取平均固定长度为n的字段"""
    pieces = [ theline[k,k+n] for k in xrange(0, len(theline),n ) ]
    if not lastfield and len(pieces[-1]) < n:
        pieces.pop()
    return pieces

# 基于index点的切割
def split_at(theline, cuts, lastfield=False):
    """cuts类似[8,16,23....]"""
    pieces = [ theline[i:j] for i,j in zip([0]+cuts, cuts+[None]) ]
    if not lastfield:
        pieces.pop()
    return pieces

"""基于生成器的形式,十分好"""
def split_at_v2(theline, cuts, lastfield=False):
    last = 0
    for cut in cuts:
        yield theline[last:cut]
        last = cut
    if lastfiled:
        yield theline[last:]

# 模拟Lc
def split_by_v2(theline, n, lastfield=False):
    return split_at_v2(theline,xrange(n, len(theline),n), lastfield)

# 未保留行之间的相对空格
def reindent(s,numspace):  
    """每行行首固定长度的空格"""
    leading = numspace * ' '
    lines  = [ leading + line.strip() for line in s.splitlines() ]
    return '\n'.join(lines)


def addSpaces(s,numAdd):   
    """增加空格，行之间相对缩进不变"""
    white = ' '*numAdd
    return white + white.join(s.splitlines(True))

def numSpaces(s):   #计算行首的空格 
    return [ len(line) - len(line.lstrip()) for line in s.splitlines()]

def delSpaces(s,numDel):
    """减少空格，行之间相对缩进不变"""
    if numDel > min(numSpaces(s)):
        raise ValueError,'Removing more space than there are!'
    return '\n'.join([line[numDel:] for line in s.splitlines()])

def unIndentBlock(s):
    """使最小缩进的行与左边缘对齐"""
    return delSpaces(s,min(numSpaces(s)))

def unexpand(astring, tablen = 8): # 切、处理、组合的方法
    """将空格转化为制表符号"""
    import re
    pieces = re.split(r'( +)', astring.expandtabs(tablen))
    lensofar = 0
    for i, piece in enumerate(pieces):
        thislen = len(piece)
        lensofar += thislen
        if piece.isspace():
            numblanks = lensofar % tablen    # ？计算的不太明白
            numtabs = (thislen - numblanks + tablen -1) / tablen
            pieces[i] = '\t' * numtabs + ' ' * numblanks
    return ''.join(pieces)

def expand_at_linestart(P, tablen):
    """只扩展行开头的制表符号"""
    import re
    def exp(m):
        return m.group().expandtabs(tablen)
    return ''.join([ re.sub(r'^\s+', exp, s) for s in P.splitlines(True) ])

def expand(formator, d, maker='"',safe=False):  # 标记
    """替换引号标记的字符串子串"""
    if safe:
        def lookup(w): return d.get(w, w.join(maker*2))
    else:
        def lookup(w): return d[w]
    parts = formator.split(maker)
    parts[1::2] = map(lookup,parts[1::2])
    return ''.join(parts)

def multiple_replace(text, adict):
    rx = re.compile('|'.join(map(re.escape, adict)))
    def translate(match):
        return adict[match.group(0)]
    return rx.sub(translate, text)

def multiple_replace_v1(*args, **kwargs):
    """闭包版本，cool"""
    adict = dict(*args, **kwargs)  # 环境
    rx = re.compile('|'.join(map(re.escape, adict)))

    def translate(match):
        return adict[match.group(0)]

    def real_replace(text):
        return rx.sub(translate, text)
    
    return real_replace

class make_multi_replace(object):
    """
    根据字典表进行替换
    """
    def __init__(self, *args, **kwargs):
        self.adict = dict(*args, **kwargs)
        self.rx = self.make_rx()

    def make_rx(self):   # 重载，使用不同的模式
        """可能需要重载，构造不同的正则表达式"""
        return re.compile('|'.join(map(re.escape, self.adict)))

    def one_xlat(self, match): # dict的value值好像都是字符串,bug
        return self.adict[ match.group(0)]

    def __call__(self, text):
        return self.rx.sub(self.one_xlat,text)

class make_multi_replace_by_word(make_multi_replace):
    def make_rx(self):
        return re.compile(r'\b%s\b' % r'\b|\b'.join(map(re.escape, self.adict)))


def anyTrue(predicate, seq):  #通用函数
    return True in itertools.imap(predicate, seq)  # 需要一项一项的检查，使用生成器，不错

def endsWith(s, *endings):   #字符串S是否以endings之一结尾
    return anyTrue(s.endswith, endings)
