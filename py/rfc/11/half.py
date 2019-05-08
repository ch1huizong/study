#! /usr/bin/env python3
# -*-coding:UTF-8 -*-
# @Time    : 2019/01/30 18:03:17
# @Author  : che
# @Email   : ch1huizong@gmail.com


import doctest


def half(x):
    """Halves x. For example:

    >>> half(6.8)
    3.4
    >>>
    """
    return x / 2


if __name__ == "__main__":
    doctest.testmod(verbose=True)
