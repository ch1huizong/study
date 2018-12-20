from twisted.internet import defer

def tee(deferred):
    """Create and return a deferred that will be fired during the
    callback/errback chain of the passed deferred. We transparently insert
    a call/errback function into the deferred's chains to trigger our new
    deferred (d).
    """
    d = defer.Deferred()
    
    def _cb(arg):
        d.callback(arg)
        return arg

    def _eb(arg):
        d.errback(arg)
        return arg

    deferred.addCallbacks(_cb, _eb)
    return d
