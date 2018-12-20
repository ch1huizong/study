#!/usr/bin/env python
# -*- coding:UTF-8 -*-

import socket

for host in ['homer','www','www.python.org','nosuchnamenamenameche']:
    print host
    try:
        hostname, aliases, addresses = socket.gethostbyname_ex(host)
        print'  Hostname:',hostname
        print'  Aliases:',aliases
        print'  Addresses:',addresses
    except socket.error as msg:
        print'ERROR:',msg
    print
