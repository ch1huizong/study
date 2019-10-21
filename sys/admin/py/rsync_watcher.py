#! /usr/bin/env python3
# -*-coding:utf-8 -*-
# @Time    : 2019/06/16 18:23:55
# @Author  : che
# @Email   : ch1huizong@gmail.com
# 线程化的目录同步工具,后台保持两个目录同步，可以进一步扩展

from threading import Timer
import sys
import time
import os
from subprocess import call
import optparse


class EventLoopDelaySpawn(object):
    def __init__(self, dir1, dir2, host="localhost", poll=10, wait=1, verbose=True):
        self.dir1 = dir1
        self.dir2 = dir2
        self.host = host
        self.poll = int(poll)
        self.wait = int(wait)
        self.verbose = verbose

    def poller(self):
        time.sleep(self.poll)
        if self.verbose:
            print("Polling at %s sec interval" % self.poll)

    def action(self):
        if self.verbose:
            print("waiting %s seconds to run Action" % self.wait)

            if self.host == "localhost" or self.host == "127.0.0.1":
                target = "%s" % self.dir2
            else:
                target = "%s:%s" % (self.host, self.dir2)

            ret = call("rsync -av --delete %s %s" % (self.dir1, target), shell=True)

        now = time.asctime()
        if ret == 0:
            print("%s : Rsync Success!" % now)
        else:
            print("%s : Rsync Failed!" % now)

    def event_handler(self):
        if os.listdir(self.dir1) != os.listdir(self.dir2):  # 这样比较只能本地, 自定义协议
            print(os.listdir(self.dir1))
            t = Timer((self.wait), self.action)  # 其实不延迟也可以
            t.start()
            if self.verbose:
                print("Event Registered")
        else:
            if self.verbose:
                print("No Event Registered")

    def run(self):
        try:
            while True:
                self.event_handler()
                self.poller()
        except Exception as err:
            print("Error: %s" % err)
        finally:
            sys.exit(0)


def main():
    p = optparse.OptionParser(
        description="后台目录同步工具",
        prog="rsync_watcher",
        version="0.1a",
        usage="%prog -s dir1 -r dir2 remote_host",
    )
    p.add_option("-s", "--source", help="local directory")
    p.add_option("-r", "--remote", help="remote directory")
    options, arguments = p.parse_args()
    if options.source and options.remote:
        if options.source.endswith("/"):
            dir1 = options.source
        else:
            dir1 = options.source + "/"
        dir2 = options.remote

        if len(arguments) == 1:
            remote_host = arguments[0]

            E = EventLoopDelaySpawn(dir1=dir1, dir2=dir2, host=remote_host)
        else:
            E = EventLoopDelaySpawn(dir1=dir1, dir2=dir2)

        E.run()
    else:
        p.print_help()


main()
