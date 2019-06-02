#! /usr/bin/env python
# -*- coding:UTF-8 -*-

try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO

import zipfile

# 列出zip压缩文件的文件或部分文件
def zip_list(filename):
    z = zipfile.ZipFile(filename,'r')
    for filename in z.namelist():
        print "File:",filename,
        content = z.read(filename)
        print "has", len(content), "bytes"

def zip_import():
    import zipfile, tempfile, os, sys
    handle, fname = tempfile.mkstemp(".zip")
    os.close(handle)
    z = zipfile.ZipFile(fname,"w")
    z.writestr("hello.py","def f(): return 'hello world from ' + __file__\n")
    z.close()
    sys.path.insert(0, fname)   # zip路径加入

    import hello       # 导入模块
    print hello.f()
    os.unlink(fname)

# 接收到一个二进制字符串，内容是zip格式内容
from zipfile import ZipFile
class ZipString(ZipFile):
    def __init__(self, datastring):
        ZipFile.__init__(self, StringIO(datastring)) # 省略建立临时.zip文件，在ZipFile打开

# 归档目录树并压缩
def make_tar(source, dest_folder, compression='bz2'):
    import tarfile, os
    if compression:
        ext = '.' + compression  # 扩展名
    else:
        ext = ''
    tarname = os.path.basename(source) + ".tar" + ext
    dest_path = os.path.join(dest_folder, tarname)  # 完整路径

    if compression:
        ztype = ':' + compression  # 扩展名
    else:
        ztype = ''
    
    out = tarfile.TarFile.open(dest_path, "w" + ztype)
    out.add(source)
    out.close()

    return dest_path



if __name__ == '__main__':
    #zip_list("log.zip")
    #zip_import()
    make_tar("/var/log/", "/tmp")  # 第一个参数字符串后面没有/,有没有/有意义


