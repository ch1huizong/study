#! /usr/bin/env python3
# -*-coding:utf-8 -*-
# @Time    : 2021/06/01 19:05:53
# @Author  : che
# @Email   : ch1huizong@gmail.com


def max(a, b):
    return a > b and a or b


def min(a, b):
    return a < b and a or b


def sum(a, b):
    return a + b


def compute(a, b, f):
    return f(a, b)


if __name__ == "__main__":
    a = int(input("请输入整数a: "))
    b = int(input("请输入整数b: "))
    print("Max a and b is", compute(a, b, max))
    print("Min a and b is", compute(a, b, min))
    print("Sum a and b is", compute(a, b, sum))
