#! /usr/bin/env python
# -*- coding:UTF-8 -*-

# 通用文件处理函数
def scanner(fileobj, linehandler):
    for line in fileobj:
        linehandler(line)

def firstword(line):
    print line.split()[0]

if __name__ == '__main__':
    # 文件对象
    f = open("data")
    scanner(f, firstword)
    f.close()

    print '-' * 60

    # 内存文件对象
    from cStringIO import StringIO
    string = StringIO('one\ntwo xxx\nthree\n')
    scanner(string, firstword)

    print '-' * 60

    # 类文件对象类,实现了特定协议
    class MyStream(object):
        def __iter__(self):
            return iter(["abc\n","b c d \n"])   # 这里可以扩展，来自不同的输入源（网络，html，数据库）
    obj = MyStream()
    scanner(obj, firstword)

