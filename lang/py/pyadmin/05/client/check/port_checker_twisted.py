#! /usr/bin/env python3
# -*-coding:utf-8 -*-
# @Time    : 2019/06/14 23:04:31
# @Author  : che
# @Email   : ch1huizong@gmail.com


import sys
from twisted.internet import reactor, protocol


class PortCheckerProtocol(protocol.Protocol):
    def __init__(self):
        print("Created a new protocol")

    def connectionMade(self):
        print("Connection made")
        reactor.stop()


class PortCheckerClientFactory(protocol.ClientFactory):
    protocol = PortCheckerProtocol

    def clientConnectionFailed(self, connector, reason):
        print("Connection failed because", reason)
        reactor.stop()


if __name__ == "__main__":
    host, port = sys.argv[1].split(":")
    factory = PortCheckerClientFactory()
    print("Testing {}".format(sys.argv[1]))
    reactor.connectTCP(host, int(port), factory)
    reactor.run()
