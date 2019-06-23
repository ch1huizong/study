# This is a simplified version of the DeferredQueue class in Twisted.
# For example purposes only!


class DeferredQueue(object):
    def __init__(self):
        self.waiting = []  # Deferreds ready for an object.
        self.pending = []  # Objects in the queue.

    def put(self, obj):
        if self.waiting:
            self.waiting.pop(0).callback(obj)
        else:
            self.pending.append(obj)

    def get(self):
        if self.pending:
            return succeed(self.pending.pop(0))
        else:
            d = Deferred()
            self.waiting.append(d)
            return d
