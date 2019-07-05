from retryingCall import RetryingCall
from twisted.web import client, error, http
from twisted.internet.error import ConnectionLost


okErrs = (http.BAD_GATEWAY, http.SERVICE_UNAVAILABLE, http.GATEWAY_TIMEOUT)


class AllowOneInternalServerError(object):
    def __init__(self):
        self.seen500 = False

    def test(self, fail):
        # Don't return a result if you want to ignore a failure that should
        # be retried.
        err = fail.trap(error.Error, ConnectionLost)
        if err is not ConnectionLost:
            status = int(fail.value.status)
            if status == http.INTERNAL_SERVER_ERROR:
                if self.seen500:
                    return fail
                else:
                    self.seen500 = True
            elif status not in okErrs:
                return fail


def userByScreenname(screenname):
    r = RetryingCall(client.getPage, screenname)
    tester = AllowOneInternalServerError()
    d = r.start(failureTester=tester.test)
    d.addCallback(lambda j: json.loads(j))
    return d
