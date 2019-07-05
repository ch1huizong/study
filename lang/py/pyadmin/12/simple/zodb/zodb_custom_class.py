#! /usr/bin/env python3
# -*-coding:utf-8 -*-
# @Time    : 2019/06/19 19:58:36
# @Author  : che
# @Email   : ch1huizong@gmail.com

import ZODB
import ZODB.FileStorage
import transaction

from account import Account


filestorage = ZODB.FileStorage.FileStorage("zodb_account.db")
db = ZODB.DB(filestorage)
conn = db.open()

root = conn.root()
che = Account("che", 1000)
print(che)
root["che"] = che
wang = Account("wang", 1000)
print(wang)
root["wang"] = wang

transaction.commit()
conn.close()
