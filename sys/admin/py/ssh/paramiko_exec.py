#! /usr/bin/env python3
# -*-coding:utf-8 -*-
# @Time    : 2019/06/14 20:33:53
# @Author  : che
# @Email   : ch1huizong@gmail.com

import paramiko

hostname = "che"
port = 22
username = ""
password = ""

if __name__ == "__main__":
    paramiko.util.log_to_file("paramiko.log")
    s = paramiko.SSHClient()
    s.load_system_host_keys()
    s.connect(hostname, port, username, password)
    stdin, stdout, stderr = s.exec_command("last")
    print(stdout.read())
    s.close()
