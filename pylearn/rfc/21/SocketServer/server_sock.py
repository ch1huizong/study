#! /usr/bin/env python
# -*- coding:UTF-8 -*-
# 基于SocketServer的服务器

import SocketServer

class MyTCPHandler1(SocketServer.BaseRequestHandler):
    
    def handle(self):
        self.data = self.request.recv(1024).strip()
        print "{} wrote:".format(self.client_address[0])
        print self.data

        self.request.sendall(self.data.upper())

class MyTCPHandler2(SocketServer.StreamRequestHandler):
        
    def handle(self):
        self.data = self.rfile.readline().strip()
        print "{} wrote:".format(self.client_address[0])
        print self.data

        self.wfile.write(self.data.upper())

class MyUDPHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        data = self.request[0].strip()
        sock = self.request[1]
        print "{} wrote:".format(self.client_address[0])
        print data

        sock.sendto(data.upper(), self.client_address)
        


if __name__ == '__main__':
    HOST, PORT = "localhost", 9999

  #  server = SocketServer.TCPServer((HOST,PORT),MyTCPHandler1)
    server = SocketServer.UDPServer((HOST,PORT),MyUDPHandler)

    server.serve_forever()
