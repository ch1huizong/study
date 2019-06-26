#! /usr/bin/env python3
# -*-coding:utf-8 -*-
# @Time    : 2019/06/14 20:33:53
# @Author  : che
# @Email   : ch1huizong@gmail.com

import paramiko
import os

hostname = "che"
port = 22
username = "root"
password = ""
dir_path = ""

if __name__ == "__main__":
    t = paramiko.Transport((hostname, port))
    t.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(t)
    files = sftp.listdir(dir_path)

    for f in files:
        print("Retrieving", f)
        sftp.get(os.path.join(dir_path, f), f)
    t.close()
