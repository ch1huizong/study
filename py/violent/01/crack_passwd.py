#! /usr/bin/env python3
# -*-coding:UTF-8 -*-
# @Time    : 2019/04/12 19:18:10
# @Author  : che
# @Email   : ch1huizong@gmail.com

import crypt


def hashpass(cryptpass, dictfile):
    salt = cryptpass[:2]
    with open(dictfile, "r") as d:
        for word in d:
            word = word.strip()
            cryptword = crypt.crypt(word, salt)
            if cryptpass == cryptword:
                print("Found Password:", word)
            else:
                print("Password not found!")


def main(passfile, dictfile, method=hashpass):
    with open(passfile, "r") as p:
        for line in p:
            user, cryptpass, *_ = line.split(":")
            print("Cracking Password For:", user)
            method(cryptpass, dictfile)
