#! /usr/bin/env python
# -*- coding:UTF-8 -*-

import paramiko

hostname = 'liufei' 
port = 22
username = 'root'
password = 'Liufei123'

if __name__ == '__main__':
    paramiko.util.log_to_file('paramiko.log')
    s = paramiko.SSHClient()
    s.load_system_host_keys()
    s.connect(hostname, port, username, password)
    stdin, stdout, stderr = s.exec_command('last')
    print stdout.read()
    s.close()
