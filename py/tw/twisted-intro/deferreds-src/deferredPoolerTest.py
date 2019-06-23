from collections import defaultdict
from operator import attrgetter

from twisted.trial import unittest
from twisted.internet import defer, reactor

from deferredPooler import DeferredPooler


class CallCounter(object):
    errString = "blah"

    def __init__(self):
        self.counts = defaultdict(int)

    @DeferredPooler
    def simple(self, *args, **kwargs):
        self.counts["simple"] += 1
        d = defer.Deferred()
        reactor.callLater(0.05, d.callback, None)
        return d

    @DeferredPooler
    @defer.inlineCallbacks
    def inlineCallbacked(self, *args, **kwargs):
        self.counts["inlineCallbacked"] += 1
        d = defer.Deferred()
        reactor.callLater(0.05, d.callback, None)
        yield d

    @DeferredPooler
    def err(self, *args, **kwargs):
        self.counts["err"] += 1
        d = defer.Deferred()
        reactor.callLater(0.05, d.errback, Exception(self.errString))
        return d


class TestDeferredpool(unittest.TestCase):
    @defer.inlineCallbacks
    def testCallSimple(self):
        func = "simple"
        counter = CallCounter()
        call = attrgetter(func)(counter)
        deferreds = [call() for _ in range(10)]
        yield defer.gatherResults(deferreds)
        self.assertEqual(1, counter.counts[func])

    @defer.inlineCallbacks
    def testCallInlineCallbacked(self):
        func = "inlineCallbacked"
        counter = CallCounter()
        call = attrgetter(func)(counter)
        deferreds = [call() for _ in range(10)]
        yield defer.gatherResults(deferreds)
        self.assertEqual(1, counter.counts[func])

    @defer.inlineCallbacks
    def testCallErr(self):
        func = "err"
        counter = CallCounter()
        call = attrgetter(func)(counter)
        n = 10
        deferreds = [call() for _ in range(n)]
        d = defer.DeferredList(deferreds, consumeErrors=True)
        results = yield d
        self.assertEqual(1, counter.counts[func])
        self.assertFalse(any([x[0] for x in results]))
        for i in range(n):
            self.assertEqual(results[i][1].value.args, (counter.errString,))
