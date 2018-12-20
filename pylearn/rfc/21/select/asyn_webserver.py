#! /usr/bin/env python
# -*- coding:UTF-8 -*-
# 异步协程服务器

import mimetypes
import os
try:
    from http.client import responses
except ImportError:
    from httplib import responses
from socket import *

from ioloop import *
from sock_yield import *

def http_server(address):
    s = CoSocket(socket(AF_INET,SOCK_STREAM))
    yield s.bind(address)
    yield s.listen(5)
    
    while True:
        conn, addr = yield s.accept()
        yield NewTask(http_request(conn, addr))
        del conn, addr

def http_request(conn, addr):
    request = b""
    while True:
        data = yield conn.recv(8192)
        request += data
        if b"\r\n\r\n" in request:
            break

    header_data = request[:request.find(b"\r\n\r\n")]
    header_text = header_data.decode('ascii')
    header_lines = header_text.splitlines()
    method, url, proto = header_lines[0].split()

    if method == 'GET':
        if os.path.exists(url[1:]):
            yield serve_file(conn, url[1:])
        else:
            yield error_response(conn, 404, "File %s not found" % url)
    else:
        yield error_response(conn, 501, "%s method not implemented" % method)
    yield conn.close()

def serve_file(conn, filename):
    content, encoding = mimetypes.guess_type(filename)
    yield conn.send(b"HTTP/1.0 200 OK\r\n")
    yield conn.send(("Content-type:%s \r\n" % content).encode('ascii'))
    yield conn.send(("Content-length:%d\r\n" %
                    os.path.getsize(filename)).encode('ascii'))
    yield conn.send(b"\r\n")
    
    f = open(filename,"rb")
    while True:
        data = f.read(8192)
        if not data:
            break
        yield conn.send(data)

def error_response(conn, code, message):
    yield conn.send(("HTTP/1.0 %d %s\r\n" %
                    (code, responses[code])).encode('ascii'))
    yield conn.send(b"Content-type: text/plain\r\n")
    yield conn.send(b"\r\n")
    yield conn.send(message.encode('ascii'))

sched = Scheduler()
sched.new(http_server(('', 8000)))
sched.mainloop()
