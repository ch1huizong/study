# -*- coding:UTF-8 -*-
from twisted.internet import defer

def got_results(res):
    print 'We got:', res

print 'Two Deferreds.'
d1 = defer.Deferred()
d2 = defer.Deferred()
d = defer.DeferredList([d1, d2])  # 会使结果顺序相同
print 'Adding Callback.'
d.addCallback(got_results)
print 'Firing d2.'
d2.callback('d2 result')
print 'Firing d1.'
d1.callback('d1 result')
