#! /usr/bin/env python
# -*- coding:UTF-8 -*-
# 提供不同格式的时间显示

from SocketServer import ThreadingMixIn, TCPServer, StreamRequestHandler
import time, socket

class TimeRequestHandler(StreamRequestHandler):
    def handle(self):
        print "Connection from", self.client_address
        request = self.rfile.readline().strip()
        if request == "asctime":
            result = time.asctime()
        elif request == "seconds":
            result = str(int(time.time()))
        elif request == "rfc822":
            result = time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime())
        else:
            result = """Unhandled request.Send a line with one of the following words:

    asctime -- for human-readable time
    seconds -- seconds since the Unix Epoch
    rfc822  -- date/time in format used for mail and news posts """
        self.wfile.write(result + "\r\n")

class TimeServer(ThreadingMixIn, TCPServer):
    allow_reuse_address = 1
    #address_family = socket.AF_INET6

serveraddr = ('', 8765)
server = TimeServer(serveraddr, TimeRequestHandler)
server.serve_forever()

        



