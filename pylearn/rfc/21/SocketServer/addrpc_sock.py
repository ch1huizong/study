#! /usr/bin/env python
# -*- coding:UTF-8 -*-

from SimpleXMLRPCServer import SimpleXMLRPCServer
from SocketServer import ForkingMixIn

class MyXMLRPCServer(ForkingMixIn, SimpleXMLRPCServer):
    def verify_request(self, request, client_address):
        host, port = client_address
        if host != '127.0.0.1':
            return False
        return SimpleXMLRPCServer.verify_request(self, request, client_address)

def add(x, y):
    return x + y

server = MyXMLRPCServer(('', 45000))
server.register_function(add)
server.serve_forever()
