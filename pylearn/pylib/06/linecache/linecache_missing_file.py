#!/usr/bin/env python
# -*- coding:UTF-8 -*-
import linecache

#Errors are even hidden if linecache cannot find the file
no_such_file=linecache.getline('no_exit.txt',1)
print'NO FILE:%r'%no_such_file
