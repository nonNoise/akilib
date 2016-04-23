
from akilib import AKI_I2C_S11059
import time

x = AKI_I2C_S11059(1)

x.Init()

print "RED = 0x%02X" % x.RED()
print "GREEN = 0x%02X" % x.GREEN()
print "BLUE = 0x%02X" % x.BLUE()
print "IR = 0x%02X" % x.IR()

while 1:
    print "R:0x%02X G:0x%02X B:0x%02X IR:0x%02X " % x.RGBISens()
    time.sleep(0.8)