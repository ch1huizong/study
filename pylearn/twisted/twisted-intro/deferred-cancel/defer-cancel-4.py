# -*- coding:UTF-8 -*-
from twisted.internet import defer

def callback(res):
    print 'callback got:', res

def errback(err):
    print 'errback got:', err

d = defer.Deferred()
d.addCallbacks(callback, errback)
d.cancel()  # 我不想要你那个结果
d.callback('result') # 是啊，取消后在激活为什么没有发生错误？
print 'done'
