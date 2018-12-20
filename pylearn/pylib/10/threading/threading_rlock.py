#!/usr/bin/env python
# encoding: UTF-8

import threading

lock=threading.RLock()

print'First try:',lock.acquire()
print'Second try:',lock.acquire(0)
