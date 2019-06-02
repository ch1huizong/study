#! /usr/bin/env python
# -*- coding:UTF-8 -*-
# 利用twisted实现的聊天服务器，需要改进吧？

from twisted.internet.protocol import Factory
from twisted.protocols.basic import LineOnlyReceiver
from twisted.internet import reactor

class Chat(LineOnlyReceiver):

    def lineReceived(self, data):
        self.factory.sendAll("%s: %s" % (self.getId(), data))

    def getId(self):
        return str(self.transport.getPeer())

    def connectionMade(self):
        print "New connection from", self.getId()
        self.transport.write("Welcome to the chat server, %s\n"% self.getId())
        self.factory.addClient(self)

    def connectionLost(self, reason):
        self.factory.delClient(self)

class ChatFactory(Factory):
    protocol = Chat

    def __init__(self):
        self.clients = []

    def addClient(self, newclient):
        self.clients.append(newclient)

    def delClient(self, client):
        self.clients.remove(client)

    def sendAll(self, message):
        for proto in self.clients:
            proto.transport.write(message + "\n")

reactor.listenTCP(51423, ChatFactory())
reactor.run()

