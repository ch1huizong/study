#! /usr/bin/env python3
# -*-coding:utf-8 -*-
# @Time    : 2019/06/14 22:23:16
# @Author  : che
# @Email   : ch1huizong@gmail.com

import paramiko
import os

hostname = ""
port = 22
username = ""
dir_path = ""
pkey_file = ""

if __name__ == "__main__":
    key = paramiko.RSAKey.from_private_key_file(pkey_file)
    t = paramiko.Transport((hostname, port))
    t.connect(username=username, pkey=key)
    sftp = paramiko.SFTPClient.from_transport(t)
    files = sftp.listdir(dir_path)

    for f in files:
        if os.path.isfile(f):
            print("Retrieving", f)
            sftp.get(os.path.join(dir_path, f), f)
    t.close()
