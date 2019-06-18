#! /usr/bin/env python3
# -*-coding:utf-8 -*-
# @Time    : 2019/06/18 16:57:30
# @Author  : che
# @Email   : ch1huizong@gmail.com

import poplib

username = ""
password = ""

mail_server = "pop.qq.com"

p = poplib.POP3(mail_server)
p.user(username)
p.pass_(password)
for msg_id in p.list()[1:]:  # 没内容？
    print(msg_id)
    outf = open('%s.eml' % msg_id.decode(), 'w')
    outf.write('\n'.join(p.retr(msg_id)[1]))
    outf.close()
p.quit()
