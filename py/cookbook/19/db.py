#! /usr/bin/env python
# -*- coding:UTF-8 -*-

import pymysql

"""时间空间使用效率比较强"""
def fetchsome(cursor, arraysize=1000):
    while True:
        results = cursor.fetchmany(arraysize)
        if not results:
            break
        for r in results:
            yield r


if __name__ == '__main__':
    c = pymysql.connect(user='root',password='quiet',database='world')
    cursor = c.cursor()

    cursor.execute('SELECT * from City')
    results = fetchsome(cursor)
    for r in results:
        print r

