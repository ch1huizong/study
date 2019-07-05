#! /usr/bin/env python3
# -*-coding:utf-8 -*-
# @Time    : 2019/06/18 23:15:21
# @Author  : che
# @Email   : ch1huizong@gmail.com

import email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import smtplib
import mimetypes


mail_server = "smtp.qq.com"
mail_port = 465
from_addr = "838431652@qq.com"
to_addr = "chehuizong@126.com"

from_header = "From: %s\r\n" % from_addr
to_header = "To: %s\r\n\r\n" % to_addr

subject_header = "Subject: Sending PDF Attachment "
attachment = "disk_report.pdf"
body = """
This message sends a PDF attachment created with Report
"""

m = MIMEMultipart()
m["To"] = to_addr
m["From"] = from_addr
m["Subject"] = subject_header
ctype, encoding = mimetypes.guess_type(attachment)
print(ctype, encoding)
maintype, subtype = ctype.split("/", 1)
print(maintype, subtype)

m.attach(MIMEText(body))
fp = open(attachment, "rb")
msg = MIMEBase(maintype, subtype)
msg.set_payload(fp.read())
fp.close()
encoders.encode_base64(msg)
msg.add_header("Content-Disposition", "attachment", filename=attachment)
m.attach(msg)

s = smtplib.SMTP_SSL(mail_server, mail_port)  # 注意这里
s.set_debuglevel(1)
s.login("838431652@qq.com", "")
s.sendmail(from_addr, to_addr, m.as_string())
s.quit()
