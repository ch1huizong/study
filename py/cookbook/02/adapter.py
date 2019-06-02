#! /usr/bin/env python
# -*- coding:UTF-8 -*-

import types, tempfile

CHUNK_SIZE = 16 * 1024

def adapter_file(fileobj):
    """某个函数需要一个真实的文件对象，而不是类文件对象"""
    if isinstance(fileobj, file):
        return fileobj
    tempobj = tempfile.TemporaryFile()
    while True:
        data = fileobj.read(CHUNK_SIZE)
        if not data:
            break
        tempobj.write(data)

    fileobj.close()
    tempobj.seek(0)
    return tempobj
