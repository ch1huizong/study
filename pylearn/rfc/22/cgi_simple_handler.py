#!/usr/bin/env python

from BaseHTTPServer import HTTPServer
from CGIHTTPServer import CGIHTTPRequestHandler
import os

os.chdir('www')

serv = HTTPServer(("",8080),CGIHTTPRequestHandler)
serv.serve_forever()
