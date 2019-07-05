#! /usr/bin/env python3
# -*-coding:utf-8 -*-
# @Time    : 2019/06/19 18:30:49
# @Author  : che
# @Email   : ch1huizong@gmail.com

import persistent


class OutOfFunds(Exception):
    pass


class Account(persistent.Persistent):
    def __init__(self, name, blance=0):
        self.name = name
        self.blance = blance

    def __str__(self):
        return "Account %s, balance %s" % (self.name, self.blance)

    def __repr__(self):
        return "Account %s, balance %s" % (self.name, self.blance)

    def deposit(self, amount):
        self.blance += amount
        return self.blance

    def withdraw(self, amount):
        if amount > self.blance:
            raise OutOfFunds
        self.blance -= amount
        return self.blance
