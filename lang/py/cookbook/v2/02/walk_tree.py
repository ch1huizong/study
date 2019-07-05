#! /usr/bin/env python
# -*- coding:UTF-8 -*-

import os
import fnmatch

def all_files(root, patterns="*", single_level=False, yield_folders=False):
    patterns = patterns.split(";")
    for path, dirs, files in os.walk(root):
        if yield_folders:
            files.extend(dirs)
        for name in files:
            for p in patterns:
                if fnmatch.fnmatch(name, p):
                    yield os.path.join(path,name)
                    break
        if single_level:
            break

def count_files(root):
    file_count = 0
    dir_count = 1
    for path, dirs, files in os.walk(root):
        for f in files: 
            file_count += 1
        for d in dirs: 
            dir_count += 1
    return "Files:%d \tDirs:%d" % (file_count, dir_count)

def swapext(root, before,after):
    """把某目录树下一类文件扩展名改为另一类"""
    if before[:1] != ".":
        before = "." + before
    if after[:1] != ".":
        after = "." + after
    extlen = len(before)

    for path, dirs, files in os.walk(root):
        for name in files:
            if name[-extlen:] == before:
                oldname = os.path.join(path,name)
                newname = oldname[:-extlen] + after
                os.rename(oldname, newname)
        
    

if __name__ == '__main__':
    #for name in all_files("/", "*.py;*.html;*.htm"):
    #    print name

    #print count_files("/")
    import sys
    if len(sys.argv) != 4:
        print "Usage: swapext root before after"
        sys.exit(100)
    swapext(sys.argv[1], sys.argv[2],sys.argv[3])
