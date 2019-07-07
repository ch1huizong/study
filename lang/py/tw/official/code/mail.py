#! /usr/bin/env python
# -*- coding:utf-8 -*-

from __future__ import print_function

import sys

from twisted.internet import protocol, defer, endpoints, task
from twisted.mail import imap4
from twisted.python import failure


@defer.inlineCallbacks
def main(reactor, username=b"", password=b"", strport="ssl:imap.qq.com:993"):
    endpoint = endpoints.clientFromString(reactor, strport)
    factory = protocol.Factory.forProtocol(imap4.IMAP4Client)
    try:
        client = yield endpoint.connect(factory)
        yield client.login(username, password)
        yield client.select("INBOX")
        info = yield client.fetchEnvelope(imap4.MessageSet(1))
        print ("First message subject:", info[1]["ENVELOPE"][1])
    except:
        print ("IMAP4 client interaction failed")
        failure.Failure().printTraceback()


task.react(main, sys.argv[1:])
