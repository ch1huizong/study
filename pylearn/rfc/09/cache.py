#! /usr/bin/env python3
# -*- coding:UTF -*-
# 数据流输出与发送目的地部分独立


def countdown(n):
    while n > 0:
        yield "T-minus %d\n" % n
        n -= 1
    yield "Kaboom!\n"


# 这里实现了一种缓冲
MAXBUFFERSIZE = 1024


def cache():
    chunks = []
    buffered_size = 0
    count = countdown(1000)
    outf = open("data", "w")

    for chunk in count:
        chunks.append(chunk)
        buffered_size += len(chunk)
        if buffered_size >= MAXBUFFERSIZE:
            outf.write("".join(chunks))
            chunks.clear()
            buffered_size = 0
    outf.write("".join(chunks))
    outf.close()


cache()
