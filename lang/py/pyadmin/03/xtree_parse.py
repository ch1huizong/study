#! /usr/bin/env python3
# -*-coding:utf-8 -*-
# @Time    : 2019/06/18 15:34:39
# @Author  : che
# @Email   : ch1huizong@gmail.com

import sys
from xml.etree import ElementTree as ET

e = ET.parse('system_profiler.xml')
for d in e.findall('/array/dict'):
    if d.find('string').text == 'SPSoftwareDataType':
        sp_data = d.find('array').find('dict')
        break
else:
    print('SPSoftwareDataType Not Found')
    sys.exit(1)

record = []
for child in sp_data.getchildren():
    record.append(child.text)
    if child.tag == 'string':
        print('%-15s -> %s' % tuple(record))
        record = []
