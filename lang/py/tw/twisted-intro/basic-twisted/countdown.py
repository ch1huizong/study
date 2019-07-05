#! /usr/bin/env python
# -*- coding:utf-8 -*-
import time


class Countdown(object):

    counter = 5

    def count(self):
        if self.counter == 0:
            reactor.stop()
        else:
            print self.counter, "..."
            self.counter -= 1
            reactor.callLater(1, self.count)
            # time.sleep(1)  # 自己加上的，效果相同，但是没有回到循环顶部
            # self.count()


from twisted.internet import reactor

reactor.callWhenRunning(Countdown().count)

print "Start!"
reactor.run()
print "Stop!"
