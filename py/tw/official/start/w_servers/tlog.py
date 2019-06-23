#! /usr/bin/env python
# -*- coding:UTF-8 -*-

from twisted.internet.protocol import Factory
from twisted.internet.endpoints import TCP4ServerEndpoint
from twisted.internet import reactor
from twisted.protocols.basic import LineReceiver


class LoggingProtocol(LineReceiver):

    def lineReceived(self, line):
        self.factory.fp.write(line + b'\n')


class LogfileFactory(Factory):

    protocol = LoggingProtocol

    def __init__(self, fileName):
        self.file = fileName

    def startFactory(self):
        self.fp = open(self.file, 'ab')

    def stopFactory(self):
        self.fp.close()


endpoint = TCP4ServerEndpoint(reactor, 8007)
endpoint.listen(LogfileFactory("log.data"))
reactor.run()
