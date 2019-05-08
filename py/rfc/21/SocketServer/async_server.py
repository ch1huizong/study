#! /usr/bin/env python
# -*- coding:UTF-8
# 基于SocketServer的服务器

import socket
import threading
import SocketServer

class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler):
    
    def handle(self):
        data = self.request.recv(1024)
        cur_thread = threading.current_thread()
        response = "{}:{}".format(cur_thread.name, data)
        self.request.sendall(response)

class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass

def client(ip, port, msg):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect((ip,port))

    try:
        sock.sendall(msg)
        response = sock.recv(1024)
        print "Received:{}".format(response)
    finally:
        sock.close()

if __name__ == '__main__':

    HOST, PORT = 'localhost',0

    server = ThreadedTCPServer((HOST,PORT),ThreadedTCPRequestHandler)
    ip, port = server.server_address

    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True
    server_thread.start()
    print "Server loop running in thread:",server_thread.name

    client(ip,port,"Hello world 1")
    client(ip,port,"Hello world 2")
    client(ip,port,"Hello world 3")

    server.shutdown()
    server.server_close()
