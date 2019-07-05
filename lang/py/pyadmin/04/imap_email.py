#! /usr/bin/env python3
# -*-coding:utf-8 -*-
# @Time    : 2019/06/18 17:04:28
# @Author  : che
# @Email   : ch1huizong@gmail.com

import imaplib


username = ""
password = ""

mail_server = "imap.qq.com"

i = imaplib.IMAP4_SSL(mail_server)
print(i.login(username, password))
print(i.select("INBOX"))
for msg_id in i.search(None, "ALL")[1][0].decode().split():
    print(msg_id)
    outf = open("/tmp/email/%s.eml" % msg_id, "w")
    outf.write(i.fetch(msg_id, "(RFC822)")[1][0][1].decode())
    outf.close()
i.logout()
