#!/usr/bin/env python

import socket,ftplib

def isUp(site):
    try:
        ftplib.FTP(site).quit()
    except socket.error:
        return False
    else: 
        return True

def filter_ftps(sites):
    return [ site for site in sites if isUp(site) ]
    #fitler(isUp,sites)   #best
