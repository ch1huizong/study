from deferredPooler import DeferredPooler
import whatever, json

def _convertResponse(response):
    return json.dumps(response)


class OriginalClass:
    def fetch(x, y):
        d = whatever.fetch(x, y)
        d.addCallback(_convertResponse)
        return d


class NewClass:
    @DeferredPooler
    def fetch(x, y):
        d = whatever.fetch(x, y)
        d.addCallback(_convertResponse)
        return d
