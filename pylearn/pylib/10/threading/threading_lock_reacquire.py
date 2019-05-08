#!/usr/bin/env python
# encoding: UTF-8

import threading

lock=threading.Lock()

print'First try:',lock.acquire()
print'Seconde try:',lock.acquire(0)
