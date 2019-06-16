#! /usr/bin/env python3
# -*-coding:utf-8 -*-
# @Time    : 2019/06/16 19:34:34
# @Author  : che
# @Email   : ch1huizong@gmail.com

import smtplib
import subprocess
import string


p = subprocess.Popen("df -h", shell=True, stdout=subprocess.PIPE)
MSG = p.stdout.read().decode()
FROM = "root@King"
TO = "chehuizong@126.com"
SUBJECT = "NIGHTLY DISK USAGE REPORT"

msg = "\r\n".join(
    ["From: %s" % FROM, "To: %s" % TO, "Subject: %s" % SUBJECT, "\r\n", MSG]
)
msg = msg.encode('utf-8')

server = smtplib.SMTP("localhost")
server.sendmail(FROM, TO, msg)
server.quit()
