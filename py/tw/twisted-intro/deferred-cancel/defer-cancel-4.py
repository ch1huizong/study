# -*- coding:utf-8 -*-
from twisted.internet import defer


def callback(res):
    print "callback got:", res


def errback(err):
    print "errback got:", err


d = defer.Deferred()
d.addCallbacks(callback, errback)
d.cancel()  # 我不想要你那个结果
d.callback("result")  # 忽略了这个结果了 
print "done"
