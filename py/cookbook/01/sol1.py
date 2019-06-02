#! /usr/bin/env python
# -*- coding:UTF-8 -*-

"""
    使字符串中某些方法对小写不敏感
    这个案例，值得研究研究。
"""
class iStr(str):
    """
    Case insensitive string class.
    Behaves just like str, except that all comparisons and lookups
    are case insensitive.
    """
    def __init__(self, *args):
        self._lowered = str.lower(self)
    def __repr__(self):
        return '%s(%s)' % (type(self).__name__, str.__repr__(self))
    def __hash__(self):
        return hash(self._lowered)
    def lower(self):
        return self._lowered

def _make_case_insensitive(name):  # 怎样使类的那些指定方法不区分大小写,完成转换
    ''' wrap one method of str into an iStr one, case-insensitive '''
    str_meth = getattr(str, name)  # 类似闭包
    def x(self, other, *args):     # 注意函数接口
        ''' try lowercasing 'other', which is typically a string, but
            be prepared to use it as-is if lowering gives problems,
            since strings CAN be correctly compared with non-strings.
        '''
        try: other = other.lower()
        except (TypeError, AttributeError, ValueError): pass
        return str_meth(self._lowered, other, *args)  
    # in Python 2.4, only, add the statement: x.func_name = name
    setattr(iStr, name, x)   # 将指定方法绑定到一个嵌套函数上
# apply the _make_case_insensitive function to specified methods 
# 这些方法的模式都需要本身和另一个字符串参数
for name in 'eq lt le gt gt ne cmp contains'.split():
    _make_case_insensitive('__%s__' % name)
for name in 'count endswith find index rfind rindex startswith'.split():
    _make_case_insensitive(name)
# note that we don't modify methods 'replace', 'split', 'strip', ...
# of course, you can add modifications to them, too, if you prefer that.
del _make_case_insensitive    # remove helper function, not needed any more


def _make_return_iStr(name):  
    """又一个辅助函数，对所有返回字符串方法的封装"""
    """与上一个类似，但封装细节不同"""
    str_meth = getattr(str, name)
    def x(*args):
        return iStr(str_meth(*args))
    setattr(iStr, name, x)

for name in 'center ljust rjust strip lstrip rstrip'.split():
    _make_return_iStr(name)


class iList(list):
    """不区分大写的字符串列表相应方法的封装"""
    def __init__(self, *args):
        list.__init__(self, *args)
        # rely on __setitem__ to wrap each item into iStr...
        self[:] = self
    wrap_each_item = iStr
    def __setitem__(self, i, v):
        if isinstance(i, slice): v = map(self.wrap_each_item, v)
        else: v = self.wrap_each_item(v)
        list.__setitem__(self, i, v)
    def append(self, item):
        list.append(self, self.wrap_each_item(item))
    def extend(self, seq):
        list.extend(self, map(self.wrap_each_item, seq))
