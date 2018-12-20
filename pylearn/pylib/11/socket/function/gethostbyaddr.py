#!/usr/bin/env python

import socket

hostname, aliases, addresses = socket.gethostbyaddr('202.43.192.109')
print'Hostname  :',hostname
print'Aliases   :',aliases
print'Addresses :',addresses

