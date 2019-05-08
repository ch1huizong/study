#! /usr/bin/env python
# -*- coding:UTF-8 -*-

import paramiko
import os

hostname = 'liufei'
port = 22
username = 'root'
password = 'Liufei123'
dir_path = '/root'

if __name__ == '__main__':
    t = paramiko.Transport((hostname, port))
    t.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(t)
    files = sftp.listdir(dir_path)

    for f in files:
        print 'Retrieving', f
        sftp.get(os.path.join(dir_path, f), f)
    t.close()
