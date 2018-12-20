#! /usr/bin/env python
# -*- coding:UTF-8 -*-

import asyncore
import socket

class site(asyncore.dispatcher):
    def __init__(self, address, sock=None):
        asyncore.dispatcher(self, sock)
        self.create_socket(socket.AF_INET,socket.SOCK_STREAM)
        self.connect(address)

    def handle_connect(self):
        self.send("GET / HTTP/1.0\r\n\r\n")




