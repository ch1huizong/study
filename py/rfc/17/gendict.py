#! /usr/bin/env python
# -*- coding:UTF-8 -*-

import itertools

# 将数据库记录映射到字典
def gen_dicts(cur):
    fields = [ d[0].lower() for d in cur.description ]
    while True:
        rows = cur.fetchmany()
        if not rows:
            break
        for row in rows:
            yield dict(itertools.izip(fields,row))
