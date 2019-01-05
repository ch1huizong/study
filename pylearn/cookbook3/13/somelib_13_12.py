#! /usr/bin/env python3
# -*-coding:UTF-8 -*-
# @Time    : 2019/01/05 11:09:50
# @Author  : che
# @Email   : ch1huizong@gmail.com

import logging

log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())


def func():
    log.critical('A Critical Error!')
    log.debug('A debug message')
