#! /usr/bin/env python3
# -*-coding:utf-8 -*-
# @Time    : 2019/06/15 15:13:31
# @Author  : che
# @Email   : ch1huizong@gmail.com

import os

from twisted.spread import pb
from twisted.internet import reactor


class PBDirLister(pb.Root):
    def remote_ls(self, directory):
        try:
            return os.listdir(directory)
        except OSError:
            return []

    def remote_ls_boom(self, directory):
        return os.listdir(directory)


if __name__ == "__main__":
    reactor.listenTCP(9876, pb.PBServerFactory(PBDirLister()))
    reactor.run()
