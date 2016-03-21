
from akilib import AKI_I2C_HDC1000
import time

adt7410 = AKI_I2C_HDC1000()
while 1:
	adt7410.Init()
	print "%6.3F 'C" % adt7410.read() 	
	time.sleep(1)
