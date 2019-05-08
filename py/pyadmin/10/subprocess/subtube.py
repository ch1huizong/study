#! /usr/bin/env python
# -*- coding:UTF-8 -*-
# 同时执行多个进程命令

import subprocess
import time
import sys


class BaseArgs(object):

    def __init__(self, *args, **kwargs): # 保存状态信息
        self.args = args
        self.kwargs = kwargs

        if self.kwargs.has_key("delay"):  # 关键是对多余的关键字参数进行处理
            self.delay = self.kwargs["delay"]
        else:
            self.delay = 0
        if self.kwargs.has_key("verbose"):
            self.verbose = self.kwargs["verbose"]
        else:
            self.verbose = False

    def run(self):
        raise NotImplementdError


class Runner(BaseArgs):
    """ 简化进程调用和运行一系列命令。

    Runner接收N个位置参数和一些关键字参数:

    [附加关键字参数]
        delay=1, 延时
        verbose=True， 详情

    使用：
        cmd = Runner("ls -l", "df -h", verbose=True, delay=3)
        cmd.run()
    """

    def run(self):
        for cmd in self.args:
            if self.verbose:
                print "Running %s with delay=%s" % (cmd, self.delay)
            time.sleep(self.delay)
            subprocess.call(cmd, shell=True)

if __name__ == "__main__":
    r = Runner("df -h", "du -h /tmp", verbose=True)
    r.run()
