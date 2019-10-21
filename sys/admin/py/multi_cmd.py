#! /usr/bin/env python3
# -*-coding:utf-8 -*-
# @Time    : 2019/06/16 11:28:16
# @Author  : che
# @Email   : ch1huizong@gmail.com
# 同时执行多个进程命令

import subprocess
import time
import sys


# 函数版本
def multi(*args):
    for cmd in args:
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        out = p.stdout.read().decode()
        print(out)


# 可复用类
class BaseArgs(object):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

        if "deleay" in self.kwargs:
            self.delay = self.kwargs["delay"]
        else:
            self.delay = 0
        if "verbose" in self.kwargs:
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
        verbose=True, 详情

    使用：
        cmd = Runner("ls -l", "df -h", verbose=True, delay=3)
        cmd.run()
    """

    def run(self):
        for cmd in self.args:
            if self.verbose:
                print(
                    "Running {cmd} with delay={delay}".format(cmd=cmd, delay=self.delay)
                )
            time.sleep(self.delay)
            subprocess.call(cmd, shell=True)


if __name__ == "__main__":
    """
    # test1
    multi("df -h", "ls -l /tmp", "tail /var/log/syslog")

    # test2
    r = Runner("df -h", "du -h /tmp", verbose=True)
    r.run()

    # usage3
    machines = ["144.202.84.88", "207.246.115.133", "66.42.66.38"]
    for machine in machines:
        r = Runner("ssh " + machine + " df -h", "ssh " + machine + " ls -l")
        r.run()

    # 进一步启发扩展
    results = fc.Client("*").service.status("httpd")
    for host, returns in results:
        if results == 0:
            fc.Client(host).reboot.reboot()
    """
