# -*- coding:utf-8 -*-
# 未捕获的异常
from twisted.internet.defer import Deferred


def callback(res):
    raise Exception("oops")


d = Deferred()

d.addCallback(callback)

d.callback("Here is your result.")

print "Finished"
