# -*- coding:UTF-8 -*-
# 类装饰器

registry = {}
def register(cls):
    register[cls.__clsid__] = cls
    return cls


@registry
class Foo(object):
    __clsid__ = "123-456"

    def bar(self):
        pass
