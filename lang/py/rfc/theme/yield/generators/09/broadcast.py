#!/usr/bin/env python 
# -*- coding:UTF-8 -*-
#
# broadcast.py
#
# Broadcast a generator source to a collection of consumers

def broadcast(source, consumers):
    for item in source:
        for c in consumers: 
            c.send(item) 


# Example
if __name__ == '__main__':

    class Consumer(object):

        def __init__(self,name):
            self.name = name

        def send(self,item):
            print self, "got", item

        def __str__(self):
            return self.name

    c1 = Consumer("Consumer 1")
    c2 = Consumer("Consumer 2")
    c3 = Consumer("Consumer 3")

    from follow import *
    lines = follow(open("run/foo/access-log"))
    broadcast(lines,[c1,c2,c3])
