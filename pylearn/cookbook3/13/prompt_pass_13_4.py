#! /usr/bin/env python3
# -*-coding:UTF-8 -*-
# @Time    : 2019/01/04 16:44:26
# @Author  : che
# @Email   : ch1huizong@gmail.com

import getpass


def svc_login(user, passwd):
    return True


user = getpass.getuser()
passwd = getpass.getpass()

if svc_login(user, passwd):
    print('Yay!')
else:
    print('Boo!')


