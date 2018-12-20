#! /usr/bin/env python
# -*- coding:UTF-8 -*-

import paramiko
import os

hostname = 'dev'
port = 22
username = 'ubuntu'
pkey_file = '/root/Documents/aws/pem/shouer.pem'  # pk文件
dir_path = '/home/ubuntu/'

if __name__ == '__main__':
    key = paramiko.RSAKey.from_private_key_file(pkey_file) # 加载pk文件，生成key
    t = paramiko.Transport((hostname, port))
    t.connect(username=username, pkey=key)  # 传递key
    sftp = paramiko.SFTPClient.from_transport(t)
    files = sftp.listdir(dir_path)

    for f in files:
        print 'Retrieving', f
        sftp.get(os.path.join(dir_path, f), f)
    t.close()
