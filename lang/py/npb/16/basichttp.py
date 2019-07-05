#! /usr/bin/env python
# -*- coding:UTF-8 -*-

from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
import time

class RequestHandler(BaseHTTPRequestHandler):
    def _writeheaders(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
    
    def do_HEAD(self):
        self._writeheaders()

    def do_GET(self):
        #time.sleep(60)
        self._writeheaders()
        self.wfile.write("<html><head><title>Test Page</title></head>\
        <body><h1 align='center'>This is a test page</h1><hr/></body></html>")

serveraddr = ('', 8765)
server = HTTPServer(serveraddr, RequestHandler)
server.serve_forever()


