# -*- coding:utf-8 -*-
# This is the Twisted Poetry Proxy, version 1.0
# 缓存代理服务器
# defer可以先激活了，再添加callback函数

import optparse

from twisted.internet.defer import Deferred, maybeDeferred
from twisted.internet.protocol import ClientFactory, ServerFactory, Protocol


def parse_args():
    usage = """usage: %prog [options] [hostname]:port

This is the Poetry Proxy, version 1.0.

  python poetry-proxy.py [hostname]:port

If you are in the base directory of the twisted-intro package,
you could run it like this:

  python twisted-server-1/poetry-proxy.py 10000

to proxy the poem for the server running on port 10000.
"""

    parser = optparse.OptionParser(usage)

    help = "The port to listen on. Default to a random available port."
    parser.add_option("--port", type="int", help=help)

    help = "The interface to listen on. Default is localhost."
    parser.add_option("--iface", help=help, default="localhost")

    options, args = parser.parse_args()

    if len(args) != 1:
        parser.error("Provide exactly one server address.")

    def parse_address(addr):
        if ":" not in addr:
            host = "127.0.0.1"
            port = addr
        else:
            host, port = addr.split(":", 1)

        if not port.isdigit():
            parser.error("Ports must be integers.")

        return host, int(port)

    return options, parse_address(args[0])


# 诗歌代理服务器 
class PoetryProxyProtocol(Protocol):
    def connectionMade(self):
        d = maybeDeferred(self.factory.service.get_poem)  # 可能诗歌也可能defer
        d.addCallback(self.transport.write)
        d.addBoth(lambda r: self.transport.loseConnection())


class PoetryProxyFactory(ServerFactory):

    protocol = PoetryProxyProtocol

    def __init__(self, service):
        self.service = service


# 创建TCP链接就可以使用它了,这里可否再简化？
class PoetryClientProtocol(Protocol):

    poem = ""

    def dataReceived(self, data):
        self.poem += data

    def connectionLost(self, reason):
        self.poemReceived(self.poem)

    def poemReceived(self, poem):
        self.factory.poem_finished(poem)


class PoetryClientFactory(ClientFactory):

    protocol = PoetryClientProtocol

    def __init__(self):
        self.deferred = Deferred()

    def poem_finished(self, poem):
        if self.deferred is not None:
            d, self.deferred = self.deferred, None
            d.callback(poem)

    def clientConnectionFailed(self, connector, reason):
        if self.deferred is not None:
            d, self.deferred = self.deferred, None
            d.errback(reason)


class ProxyService(object):

    poem = None  # the cached poem

    def __init__(self, host, port):
        self.host = host
        self.port = port

    def get_poem(self):
        if self.poem is not None:
            print "Using cached poem."
            return self.poem

        # 接下来是怎么样抓取诗歌
        print "Fetching poem from server."
        factory = PoetryClientFactory()
        factory.deferred.addCallback(self.set_poem)
        from twisted.internet import reactor
        reactor.connectTCP(self.host, self.port, factory)  # 代理创建到诗歌服务器的连接
        return factory.deferred

    def set_poem(self, poem):
        self.poem = poem
        return poem


def main():
    options, server_addr = parse_args()

    service = ProxyService(*server_addr)

    factory = PoetryProxyFactory(service) # 这一个代理协议工厂

    from twisted.internet import reactor

    # 接下来开启代理服务器，使用了代理协议工厂
    port = reactor.listenTCP(options.port or 0, factory, interface=options.iface)

    print "Proxying %s on %s." % (server_addr, port.getHost())

    reactor.run()


if __name__ == "__main__":
    main()
