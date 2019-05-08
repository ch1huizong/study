#! /usr/bin/env python
# -*- coding:UTF-8 -*-

import smtplib
import subprocess
import string

p = subprocess.Popen('df -h', shell=True, stdout=subprocess.PIPE)
MSG = p.stdout.read()
FROM = 'root@K'
TO = 'chehuizong@126.com'
SUBJECT = 'NIGHTLY DISK USAGE REPORT'
msg = string.join([
    'From: %s' % FROM,
    'To: %s' % TO,
    'Subject: %s' % SUBJECT,
    "",
    MSG], "\r\n")

server = smtplib.SMTP('localhost')
server.sendmail(FROM, TO, msg)
server.quit()
