#! /usr/bin/env python
# -*- coding:UTF-8 -*-
# 多线程SimpleHttp服务器

from BaseHTTPServer import HTTPServer
from SocketServer import ThreadingMixIn
from SimpleHTTPServer import SimpleHTTPRequestHandler

class ThreadingServer(ThreadingMixIn, HTTPServer):
    pass

serveraddr = ('', 8765)
server = ThreadingServer(serveraddr, SimpleHTTPRequestHandler)
server.serve_forever()

