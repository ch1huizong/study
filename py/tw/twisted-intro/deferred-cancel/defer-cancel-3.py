# -*- coding:utf-8 -*-
from twisted.internet import defer


def callback(res):
    print "callback got:", res


def errback(err):
    print "errback got:", err


d = defer.Deferred()
d.addCallbacks(callback, errback)
d.callback("result")
d.cancel()  # 取消一个已经被激发的defer，没有效果
print "done"
