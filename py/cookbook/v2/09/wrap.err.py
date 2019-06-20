#! /usr/bin/env python
# -*- coding:UTF-8 -*-
# 同步一个对象中的所有方法,
# 既在多个线程中只有对象的一个方法调用结束后，
# 同一对象中另一个方法才能被别的线程使用

def wrap_callable(any_callable, before, after):
    def _wrapped(*a, **kw):
        before()
        try:
            return any_callable(*a, **kw)
        except:
            after()
        _wrapped.__name__ = any_callable.__name__
        return _wrapped

import inspect
class GenericWrapper(object):

    def __init__(self, obj, before, after, ignore=()):
        classname = "GenericWrapper"
        self.__dict__['_%s__methods'% classname] = {}
        self.__dict__['_%s__obj'% classname] = obj
        for name, method in inspect.getmembers(obj, inspect.ismethod):
            if name not in ignore and method not in ignore:
                self.__methods[name] = wrap_callable(method, before, after)

    def __getattr__(self, name):
        try:
            return self.__methods[name]
        except KeyError:
            return getattr(self.__obj, name)

    def __setattr__(self, name, value):
        setattr(self.__obj, name, value)

class SynchronizedObject(GenericWrapper):
    def __init__(self, obj, ignore=(), lock=None):
        if lock is None:
            import threading
            lock = threading.RLock()
        GenericWrapper.__init__(self, obj, lock.acquire, lock.release, ignore)

if __name__ == '__main__':
    import threading
    import time
    class Dummy(object):

        def foo(self):
            print "Hello from foo"
            time.sleep(1)

        def bar(self):
            print "Hello from bar"

        def baaz(self):
            print "Hello from baaz"

    tw = SynchronizedObject(Dummy(), ignore=('baaz',))
    threading.Thread(target=tw.foo).start()
    time.sleep(0.1)
    threading.Thread(target=tw.bar).start()
    time.sleep(0.1)
    threading.Thread(target=tw.baaz).start()


