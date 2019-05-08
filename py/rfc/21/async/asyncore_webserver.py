#! /usr/bin/env python
# -*- coding:UTF-8 -*-

import asyncore, socket
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
class async_http_handler(asyncore.dispatcher):
    def __init__(self, sock=None):
        asyncore.dispatcher.__init__(self,sock)
        self.got_request = False
        self.request_data = b""
        self.write_queue = collections.deque()
        self.responding = False

    def readable(self): # 未获得请求前
        return not self.got_request

    def handle_read(self):
        chunk = self.recv(8192)
        self.request_data += chunk
        if b"\r\n\r\n" in self.request_data:
            self.handle_request()

    def handle_request(self):
        self.got_request = True
        header_data = self.request_data[:self.request_data.find(b"\r\n\r\n")]
        header_text = header_data.decode("ascii")
        header_lines = header_text.splitlines()
        #print header_lines[0] + "\r\n"
        request = header_lines[0].split()
        method = request[0]
        url = request[1][1:]
        self.process_request(method, url)

    def process_request(self, method, url):
        self.responding = True
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
                self.push(open(url,"rb").read())
        else:
            self.send_error(501,"%s method not implemented" % method)
    
    def send_error(self, code, message):
        self.push_text("HTTP/1.0 %s %s \r\n" % (code, responses[code]))
        self.push_text("Content-type: text/plain\r\n")
        self.push_text("\r\n")
        self.push_text(message)

    def push(self, data):
        self.write_queue.append(data)

    def push_text(self, text):
        self.push(text.encode("ascii"))

    # 仅在响应准备好时才能写入
    def writable(self):
        return self.responding and self.write_queue

    def handle_write(self):
        chunk = self.write_queue.popleft()
        bytes_sent = self.send(chunk)
        if bytes_sent != len(chunk):  # 发送了小片段
            self.write_queue.appendleft(chunk[bytes_sent:])
        if not self.write_queue:
            self.close()

a = async_http(8080)
asyncore.loop()
