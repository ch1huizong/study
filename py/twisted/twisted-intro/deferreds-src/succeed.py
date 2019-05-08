# This is a simplified version of code that's in Twisted.
# For example purposes only!

def succeed(result):
    d = Deferred()
    d.callback(result)
    return d


def fail(result=None):
    d = Deferred()
    d.errback(result)
    return d
