#! /usr/bin/env python
# -*- coding:UTF-8 -*-
# 多任务处理的thread版本
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from SocketServer import ThreadingMixIn
import time
import threading

starttime = time.time()

class RequestHandler(BaseHTTPRequestHandler):
    def _writeheaders(self, doc):
        if doc is None:
            self.send_response(404)
        else:
            self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
   
    def _getdoc(self, filename):
        global starttime
        if filename == "/":
            return """<html><head><title>Test Page</title></head>\
                    <body><h1 align='center'>This is a Test Page</h1><br\>\
                    <p align="right">you can look at the <a href="stats.html">\
                    server statistics</a></p><hr/></body></html>"""

        elif filename == "/stats.html":
            return """<html><head><title>Statistics</title></head><body>This\
                    Server has been Running for %d seconds<hr/></body></html>"""\
                    % int(time.time() - starttime)

        else:
            return None
        
    def do_HEAD(self): # 只发送头
        doc = self._getdoc(self.path)
        self._writeheaders(doc)

    def do_GET(self):
        print "Handling with thread", threading.currentThread().getName()

        doc = self._getdoc(self.path)
        self._writeheaders(doc)

        if doc is None:
            self.wfile.write("""<html><head><title>Not Found</title></head>\
            <body>The requested document '%s' was not found.</body></html> """\
            % self.path)
        else:
            self.wfile.write(doc)

class ThreadingHTTPServer(ThreadingMixIn, HTTPServer):
    pass

serveraddr = ('', 8765)
server = ThreadingHTTPServer(serveraddr, RequestHandler)
server.serve_forever()
