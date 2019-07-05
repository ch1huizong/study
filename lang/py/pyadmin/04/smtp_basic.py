#! /usr/bin/env python3
# -*-coding:utf-8 -*-
# @Time    : 2019/06/18 22:40:16
# @Author  : che
# @Email   : ch1huizong@gmail.com

import smtplib

mail_server = "localhost"
mail_port = 25
from_addr = "838431652@qq.com"
to_addr = "chehuizong@126.com"

from_header = "From: %s\r\n" % from_addr
to_header = "To: %s\r\n\r\n" % to_addr
subject_header = "Subject: nothing interesting"
body = "This is a not very interesting email."
email_message = "%s\n%s\n%s\n\n%s" % (from_header, to_header, subject_header, body)

s = smtplib.SMTP(mail_server, mail_port)
s.sendmail(from_addr, to_addr, email_message)
s.quit()
