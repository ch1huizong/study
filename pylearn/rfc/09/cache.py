#! /usr/bin/env python
# -*- coding:UTF -*-
# 利用yield生成输出流，发送至文件或网络

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
    
    outf = open("data","w")

    for i,chunk in enumerate(count):
        chunks.append(chunk)
        buffered_size += len(chunk)
        if buffered_size >= MAXBUFFERSIZE:
            outf.write("".join(chunks) + "Cache Block %d\n"% i)
            chunks = []
            buffered_size = 0
    outf.write("".join(chunks)) # 剩余的
    outf.close()

cache()
