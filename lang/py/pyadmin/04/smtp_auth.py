#! /usr/bin/env python3
# -*-coding:utf-8 -*-
# @Time    : 2019/06/18 23:00:18
# @Author  : che
# @Email   : ch1huizong@gmail.com

import smtplib

mail_server = "smtp.qq.com"
mail_port = 465
from_addr = "838431652@qq.com"
to_addr = "chehuizong@126.com"

from_header = "From: %s\r\n" % from_addr
to_header = "To: %s\r\n\r\n" % to_addr
subject_header = "Subject: Testing SMTP Authentication"
body = "This mail tests SMTP Authentication "
email_message = "%s\n%s\n%s\n\n%s" % (from_header, to_header, subject_header, body)

s = smtplib.SMTP_SSL(mail_server, mail_port)  # 注意这里
s.set_debuglevel(1)
s.login("838431652@qq.com", "")
s.sendmail(from_addr, to_addr, email_message)
s.quit()
