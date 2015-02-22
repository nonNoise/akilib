# -*- encoding:utf8 -*-
import mraa
import time
from struct import *
from akilib import AKI_I2C_HDC1000
import datetime


x = AKI_I2C_HDC1000.AKI_I2C_HDC1000()

x.Config()


print '-' * 20

while 1:
	print "%d C" % x.Temperature()
	print u"%d /" % x.Humidity()

	print '-' * 20
	time.sleep(0.1)
#print "0x%04X" % x.Humidity()

print '-' * 20




