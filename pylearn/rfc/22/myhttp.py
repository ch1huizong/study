#!/usr/bin/env python

import os

try:
    from http.server import HTTPServer              #python3
    from socketserver import ThreadingMixIn
except ImportError:
    from BaseHTTPServer import HTTPServer,BaseHTTPRequestHandler   #python2
    from SocketServer import ThreadingMixIn

class MyHTTPServer(ThreadingMixIn,HTTPServer):
    def __init__(self,addr,handler,subnet):
        HTTPServer.__init__(self,addr,handler)
        self.subnet = subnet
    def verify_request(self,request,client_address):
        host, port = client_address                         #auto fill??
        if not host.startswith(self.subnet):
            return False
        return HTTPServer.verify_request(self,request,client_address)

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        filename = os.path.basename(self.path[1:])
        f = open(filename,'r')
        self.wfile.write(f.read())
        f.close()
        


serv = MyHTTPServer(('',8080),MyHandler,'127.0.0.')
serv.serve_forever()

