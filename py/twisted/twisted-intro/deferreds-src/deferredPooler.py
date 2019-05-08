from twisted.internet import defer
from twisted.python import failure


class DeferredPooler(object):
    def __init__(self, func):
        self._func = func
        self._pool = {}

    def _callOthers(self, result, key):
        if isinstance(result, failure.Failure):
            for d in self._pool[key]:
                d.errback(result)
        else:
            for d in self._pool[key]:
                d.callback(result)
        del self._pool[key]
        return result

    def _call(self, instance, *args, **kwargs):
        key = (args, hash(tuple(sorted(kwargs.items()))))
        if key in self._pool:
            d = defer.Deferred()
            self._pool[key].append(d)
            return d
        else:
            self._pool[key] = []
            d = self._func(instance, *args, **kwargs)
            assert isinstance(d, defer.Deferred)
            d.addBoth(self._callOthers, key)
            return d
 
    def __get__(self, instance, owner):
        def wrapper(*args, **kwargs):
            return self._call(instance, *args, **kwargs)
        return wrapper
