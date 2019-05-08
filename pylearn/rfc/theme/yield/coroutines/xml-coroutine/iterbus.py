#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#
# iterbus.py
#
# 使用解析树
# An example of incremental XML parsing with the ElementTree library

from xml.etree.cElementTree import iterparse

for event, elem in iterparse("allroutes.xml",('start','end')):

    if event == 'start' and elem.tag == 'buses':
        buses = elem

    elif event == 'end' and elem.tag == 'bus':
        busdict = dict((child.tag,child.text) for child in elem)

        if busdict['route'] == '22' and busdict['direction'] == 'North Bound':
            print "%(id)s,%(route)s,\"%(direction)s\","\
                  "%(latitude)s,%(longitude)s" % busdict

        buses.remove(elem) # buses删除这个bus元素
