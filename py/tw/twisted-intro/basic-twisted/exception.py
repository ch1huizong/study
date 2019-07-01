#! /usr/bin/env python
# -*- coding:utf-8 -*-


def falldown():
    raise Exception("I fall down.")


def upagain():
    print "But I get up again."
    reactor.stop()


from twisted.internet import reactor

reactor.callWhenRunning(falldown) # 会回到顶部重新回调吗？
reactor.callWhenRunning(upagain)

print "Starting the reactor."
reactor.run()
