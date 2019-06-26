#! /usr/bin/env python3
# -*-coding:utf-8 -*-
# @Time    : 2019/06/19 18:57:07
# @Author  : che
# @Email   : ch1huizong@gmail.com

import ZODB
import ZODB.FileStorage
import transaction

from account import Account, OutOfFunds


filestorage = ZODB.FileStorage.FileStorage("zodb_account.db")
db = ZODB.DB(filestorage)
conn = db.open()

root = conn.root()
che = root["che"]
print("Before Withdraw")
print("=" * 60)
print(che)
wang = root["wang"]
print(wang)
print("-" * 60)

while True:
    try:
        transaction.begin()
        che.withdraw(300)
        wang.deposit(300)
        transaction.commit()
    except OutOfFunds:
        print("OutOfFunds Error")
        print("Current account information")
        print(che)
        print(wang)
        transaction.abort()
        break


print("\nAfter Withdraw")
print("=" * 60)
print(che)
print(wang)
print("-" * 60)

conn.close()
