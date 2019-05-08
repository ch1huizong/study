#! /usr/bin/env python
# -*- coding:UTF-8 -*-

import paramiko

hostname = 'dev'
port = 22
username = 'ubuntu'
key_filename = '/root/aws/pem/shouer.pem'
#pkey_file = '/root/.ssh/id_rsa'

if __name__ == '__main__':
    #key = paramiko.RSAKey.from_private_key_file(pkey_file)
    s = paramiko.SSHClient()
    s.load_system_host_keys() # 不加载会有什么后果?
    #s.connect(hostname, port, pkey=key)
    s.connect(hostname, port, username, key_filename=key_filename)
    stdin, stdout, stderr = s.exec_command('last')
    print stdout.read()
    s.close()
