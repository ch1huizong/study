#! /usr/bin/env python
# -*- coding:UTF-8 -*-

import threading

class TestThread(threading.Thread):

    def __init__(self, name="TestThread"):
        self._stopevent = threading.Event()
        self._sleepperiod = 1.0
        threading.Thread.__init__(self,name=name)

    def run(self):
        print "%s starts"% (self.getName(),)
        count = 0
        while not self._stopevent.is_set(): #note
            count += 1
            print "loop %d"%(count,)
            self._stopevent.wait(self._sleepperiod)
        print "%s ends"% (self.getName(),)

    def join(self, timeout=None):
        self._stopevent.set()
        threading.Thread.join(self, timeout)  # note

if __name__ == '__main__':
    t = TestThread()
    t.start()
    import time
    time.sleep(5)
    t.join()



