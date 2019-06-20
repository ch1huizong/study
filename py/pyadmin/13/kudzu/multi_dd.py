#! /usr/bin/env python3
# -*-coding:utf-8 -*-
# @Time    : 2019/06/20 11:30:40
# @Author  : che
# @Email   : ch1huizong@gmail.com

import subprocess
import optparse


class ImageFile(object):
    def __init__(self, num=None, size=None, dest=None):
        self.num = num
        self.size = size
        self.dest = dest

    def create_image(self):
        for i in range(self.num):
            try:
                cmd = "dd if=/dev/zero of=%s/file.%s bs=1024 count=%s" % (
                    self.dest,
                    i,
                    self.size,
                )
                subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
            except Exception as e:
                print(e)

    def controller(self):
        p = optparse.OptionParser(
            description="Launches Many dd",
            prog="muti_dd",
            version="0.1",
            usage="%prog [options] dest",
        )
        p.add_option("-n", "--number", help="set many dd", type=int)
        p.add_option("-s", "--size", help="size of image in bytes", type=int)
        p.set_defaults(number=10, size=10240)  # 注意这里size的具体含义

        options, arguments = p.parse_args()
        if len(arguments) == 1:
            self.dest = arguments[0]
            self.size = options.size
            self.num = options.number
            self.create_image()


def main():
    start = ImageFile()
    start.controller()


if __name__ == "__main__":
    main()
