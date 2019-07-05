#! /usr/bin/env python3
# -*-coding:utf-8 -*-
# @Time    : 2019/06/19 18:11:27
# @Author  : che
# @Email   : ch1huizong@gmail.com

import ZODB
import ZODB.FileStorage
import transaction

filestorage = ZODB.FileStorage.FileStorage("zodb.db")
db = ZODB.DB(filestorage)
conn = db.open()

root = conn.root()
root["list"] = ["This", "is", "a ", "list"]
root["dict"] = {"This": "is", "a": "dictionary"}

transaction.commit()
conn.close()
