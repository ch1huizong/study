# -*- coding:utf-8 -*-

from twisted.internet.defer import inlineCallbacks, Deferred


@inlineCallbacks  # 装饰器函数返回一个大defer
def my_callbacks():
    from twisted.internet import reactor

    print "first callback"
    result = yield 1  # yielded values that aren't deferred, come right back

    print "second callback got", result
    d = Deferred()
    reactor.callLater(5, d.callback, 2)  # 超时到达（or数据到达）激活defer
    result = yield d  # yielded deferreds will pause the generator

    print "third callback got", result  # the result of the deferred

    d = Deferred()
    reactor.callLater(5, d.errback, Exception(3))

    try:
        yield d
    except Exception, e:
        result = e

    print "fourth callback got", repr(result)  # the exception from the deferred

    reactor.stop()


from twisted.internet import reactor

reactor.callWhenRunning(my_callbacks)
reactor.run()
