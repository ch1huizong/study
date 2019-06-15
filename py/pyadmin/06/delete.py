#! /usr/bin/env python3
# -*-coding:utf-8 -*-
# @Time    : 2019/06/15 19:04:25
# @Author  : che
# @Email   : ch1huizong@gmail.com

import os


class Delete(object):
    def __init__(self, file):
        self.file = file

    def interactive(self):
        choice = input("Do you really want to delete %s [N]/Y? " % self.file)
        if choice.upper():
            print("DELETING: %s" % self.file)
            status = os.remove(self.file)
        else:
            print("Skipping: %s" % self.file)

    def dryrun(self):
        print("Dry Run: %s [NOT DELETED]" % self.file)

    def delete(self):
        print("DELETING: %s" % self.file)
        try:
            status = os.remove(self.file)
        except Exception as e:
            print(err)


if __name__ == "__main__":
    from dupe import find_dupes

    dupes = find_dupes("tmp")

    for d in dupes:
        delete = Delete(d)
        #delete.dryrun()
        #delete.interactive()
        delete.delete()
