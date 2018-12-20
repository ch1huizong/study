#! /usr/bin/env python
# -*- coding:UTF-8 -*-

from SocketServer import TCPServer, StreamRequestHandler
import time

class TimeServerHandler(StreamRequestHandler):
    def handle(self):
        print "Got connection from %s" % str(self.client_address)
        resp = time.ctime() + '\r\n\r\n'
        self.wfile.write(resp.encode('ascii'))

if __name__ == '__main__':
    s = TCPServer(('', 9999), TimeServerHandler)
    s.serve_forever()

