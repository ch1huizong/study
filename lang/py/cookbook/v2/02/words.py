#! /usr/bin/env python
# -*- coding:UTF-8 -*-

"""迭代器产生词，可以指定分词函数"""

def gen_words(thefile, line_to_words = str.split()): # 注意，分词的函数
    f = open(thefile)
    for line in f:
        for word in line_to_words(line):
            yield word
    f.close()

import re
def gen_words_by_re(thefile, pattern = r"[\w'-]"):
    wre = re.compile(pattern)
    def line_to_words(line):
        for m in wre.finditer(line):
            return m.group(0)
    return gen_words(thefile, line_to_words)
    

