# -*- coding:UTF-8 -*-

class DocMeta(type):

    def __init__(self, name, bases, dict):
        for key, value in dict.items():
            if key.startswith('__'):
                continue
            if not hasattr(value, '__call__'):
                continue
            if not getattr(value, '__doc__'):
                raise TypeError('%s must have a docstring' % key)
        type.__init__(self, name, bases, dict)


class Documented(metaclass=DocMeta): # 基类
    pass


class Foo(Documented):
    def spam(self, a, b): 
        pass

