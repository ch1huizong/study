#! /usr/bin/env python3
# -*-coding:UTF-8 -*-
# @Time    : 2019/01/29 17:59:08
# @Author  : che
# @Email   : ch1huizong@gmail.com

import socket


class Client(object):

    """Pickle Sock"""

    def __init__(self, addr):
        self.server_addr = addr
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect(addr)

    def __getstate__(self):
        return self.server_addr

    def __setstate__(self, value):
        self.server_addr = value
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect(self.server_addr)
