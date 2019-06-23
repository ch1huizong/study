#! /usr/bin/env python
# -*- coding:utf-8 -*-


def falldown():
    raise Exception("I fall down.")


def upagain():
    print "But I get up again."
    reactor.stop()


from twisted.internet import reactor

reactor.callWhenRunning(falldown)
reactor.callWhenRunning(upagain)  # 再次调用时不会再调用上个

print "Starting the reactor."
reactor.run()
