#!/usr/bin/env python

import time
import os

def show_zone_info():
	print'	TZ	:',os.environ.get('TZ','(not set)')
	print'	tzname:	',time.tzname
	print'	Zone	:%d (%d)'%(time.timezone,(time.timezone/3600))
	print'	DST	:',time.daylight
	print'	Time	:',time.ctime()
	print

print'Default:'
show_zone_info()

ZONES = ['GMT',
		  'Europe/Amsteradm',
		]

for zone in ZONES:
	os.environ['TZ'] = zone
	time.tzset()
	print zone,':'
	show_zone_info()

