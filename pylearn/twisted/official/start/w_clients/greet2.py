#! /usr/bin/env python
# -*- coding:UTF-8 -*-
# 哪里发送数据？

from twisted.internet.protocol import Protocol, ReconnectingClientFactory
from twisted.internet import reactor
from sys import stdout

class Echo(Protocol):
    def dataReceived(self, data):
        stdout.write(data)


class EchoClientFactory(ReconnectingClientFactory):
    def startedConnecting(self, connector):
        print('Started to connect.')

    def buildProtocol(self, addr):
        print('Connected.')
        print('Resetting reconnection delay')
        self.resetDelay()
        return Echo()

    def clientConnectionLost(self, connector, reason):
        print('Lost connection.  Reason:', reason)
        ReconnectingClientFactory.clientConnectionLost(self, connector, reason)

    def clientConnectionFailed(self, connector, reason):
        print('Connection failed. Reason:', reason)
        ReconnectingClientFactory.clientConnectionFailed(self, connector,
                                                         reason)

reactor.connectTCP("localhost", 1234, EchoClientFactory())
reactor.run()
