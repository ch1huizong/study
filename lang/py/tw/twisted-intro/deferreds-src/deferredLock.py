# This is a simplified version of the DeferredLock class in Twisted.
# For example purposes only!


class DeferredLock(object):

    locked = False

    def __init__(self):
        self.waiting = []  # Deferreds that are wanting the lock.

    def acquire(self):
        d = Deferred()
        if self.locked:
            self.waiting.append(d)
        else:
            self.locked = True
            d.callback(self)
        return d

    def release(self):
        assert self.locked, "Tried to release an unlocked lock"
        self.locked = False
        if self.waiting:
            # someone is waiting to acquire lock
            self.locked = True
            d = self.waiting.pop(0)
            d.callback(self)
