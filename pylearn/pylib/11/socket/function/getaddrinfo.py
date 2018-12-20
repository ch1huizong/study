#! /usr/bin/env python
# -*- coding:UTF-8 -*-

import socket

def get_constants(prefix):
    return dict( (getattr(socket,name),name)      # (value,name)
            for name in dir(socket) 
            if name.startswith(prefix))

families = get_constants('AF_')
types = get_constants('SOCK')
protocols = get_constants('IPPROTO_')

for response in socket.getaddrinfo('www.python.org','http'):
    family, socktype, proto, canonname, sockaddr = response

    print 'Family       :', families[family]
    print 'Type         :', types[socktype]
    print 'Protocol     :', protocols[proto] 
    print 'Canonical name:', canonname
    print 'Socket address:', sockaddr
    print 



