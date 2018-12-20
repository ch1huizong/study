#! /usr/bin/env python
# -*- coding:UTF-8 -*-

import asynchat, asyncore, socket
import os
import mimetypes
import collections
try:
    from http.client import responses
except ImportError:
    from httplib import responses

# 监控套接字
class async_http(asyncore.dispatcher):
    def __init__(self, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind(('', port))
        self.listen(5)
    
    def handle_accept(self):
       client, addr = self.accept()
       return async_http_handler(client)

# 客户端套接子，处理客户端
class async_http_handler(asynchat.async_chat):
    def __init__(self, sock=None):
        asynchat.async_chat.__init__(self, sock) 
        self.data = []
        self.got_header = False
        self.set_terminator(b"\r\n\r\n")

    def collect_incoming_data(self, data):
        if not self.got_header:
            self.data.append(data)

    # 到达终止符号
    def found_terminator(self):
        self.got_header = True
        header_data = b"".join(self.data) 
        header_text = header_data.decode("ascii")
        header_lines = header_text.splitlines()
        request = header_lines[0].split()
        method = request[0]
        url = request[1][1:]
        self.process_request(method, url)

    def process_request(self, method, url):
        if method == "GET":
            if not os.path.exists(url):
                self.send_error(404, "File %s not found\r\n" % url)
            else:
                type, encoding = mimetypes.guess_type(url)
                size = os.path.getsize(url)
                self.push_text("HTTP/1.0 200 OK\r\n")
                self.push_text("Content-length:%d\r\n" % size)
                self.push_text("Content-type: %s\r\n" % type)
                self.push_text("\r\n")
                self.push_with_producer(file_producer(url))
        else:
            self.send_error(501,"%s method not implemented" % method)
        self.close_when_done()
    
    def send_error(self, code, message):
        self.push_text("HTTP/1.0 %s %s \r\n" % (code, responses[code]))
        self.push_text("Content-type: text/plain\r\n")
        self.push_text("\r\n")
        self.push_text(message)

    def push_text(self, text):
        self.push(text.encode("ascii"))

class file_producer(object):
    def __init__(self, filename, buffer_size=512):
        self.f = open(filename,'rb')
        self.buffer_size = buffer_size

    def more(self):
        data = self.f.read(self.buffer_size)
        if not data:
            self.f.close()
        return data

a = async_http(8080)
asyncore.loop()
