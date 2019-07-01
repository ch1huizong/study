# -*- coding:utf-8 -*-
from twisted.internet.defer import Deferred


def send_poem(d):
    print "Sending poem"
    d.callback("Once upon a midnight dreary")


def get_poem():
    """Return a poem 5 seconds later."""

    def canceler(d):
        # They don't want the poem anymore, so cancel the delayed call
        delayed_call.cancel()  # 延时调用取消了

        # At this point we have three choices:
        #   1. Do nothing, and the deferred will fire the errback
        #      chain with CancelledError.
        #   2. Fire the errback chain with a different error.
        #   3. Fire the callback chain with an alternative result.

    d = Deferred(canceler)

    from twisted.internet import reactor

    delayed_call = reactor.callLater(5, send_poem, d)  # 保存延时调用

    return d


def got_poem(poem):
    print "I got a poem:", poem


def poem_error(err):
    print "get_poem failed:", err


def main():
    from twisted.internet import reactor

    reactor.callLater(10, reactor.stop)  # stop the reactor in 10 seconds

    d = get_poem()
    d.addCallbacks(got_poem, poem_error)

    reactor.callLater(2, d.cancel)  # cancel after 2 seconds

    reactor.run()


main()
