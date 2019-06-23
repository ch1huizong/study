# -*- coding:utf-8 -*-
# 可以接收信息的回调


class Malfunction(Exception):
    pass


def my_generator():
    print "starting up"

    val = yield 1
    print "got:", val

    val = yield 2
    print "got:", val

    try:
        yield 3
    except Malfunction:
        print "malfunction!"

    yield 4

    print "done"


gen = my_generator()

print gen.next()  # start the generator ...1
print gen.send(10)  # send the value 10 ...2
print gen.send(20)  # send the value 20 ...3
print gen.throw(Malfunction())  # raise an exception inside the generator

try:
    gen.next()
except StopIteration:
    pass
