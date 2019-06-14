#! /usr/bin/env python3
# -*-coding:utf-8 -*-
# @Time    : 2019/06/14 21:13:29
# @Author  : che
# @Email   : ch1huizong@gmail.com

import paramiko

hostname = "108.61.215.120"
port = 22
username = "root"
pkey_file = "/root/id_rsa"

if __name__ == "__main__":
    key = paramiko.RSAKey.from_private_key_file(pkey_file)
    s = paramiko.SSHClient()
    s.load_system_host_keys()
    s.connect(hostname, port, pkey=key)
    stdin, stdout, stderr = s.exec_command("ifconfig")
    print(stdout.read())
    s.close()
