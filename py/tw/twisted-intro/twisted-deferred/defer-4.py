# -*- coding:utf-8 -*-
from twisted.internet.defer import Deferred


def out(s):
    print s


d = Deferred()
d.addCallbacks(out, out)
d.callback("First result")
d.callback("Second result")  # 不允许被激活两次
print "Finished"
