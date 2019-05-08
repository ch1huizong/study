# -*- coding:UTF-8 -*-

import time


class Date(object):

    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod # 与类有关的属性
    def now(cls):
        t = time.localtime()
        return cls(t.tm_year, t.tm_mon, t.tm_mday)

    @classmethod
    def tomorrow(cls):
        t = time.localtime(time.time()+86400)
        return cls(t.tm_year, t.tm_mon, t.tm_mday)

    def __str__(self):
        return "%04d-%02d-%02d" % (self.year, self.month, self.day)


class EuroDate(Date):

    def __str__(self):
        return "%02d/%02d/%04d" % (self.day,self.month,self.year)


# 类方法
class Times(object):
    factor = 1

    @classmethod
    def mul(cls, x):
        return cls.factor * x


class TwoTimes(Times):
    factor = 2
