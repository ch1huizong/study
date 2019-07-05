#!/usr/bin/env python
# encoding: UTF-8
import threading

#method 1
def func():
    print'func() passed to Thread'

t=threading.Thread(target=func)
t.start()


#method 2
class Mythread(threading.Thread):
    def run(self):
        print'Mythread extended from Thread'

t=Mythread()
t.start()
