
import time
from akilib.edison import AKI_I2C_L3GD20


L3GD20 = AKI_I2C_L3GD20.AKI_I2C_L3GD20(1)

time.sleep(0.01)
L3GD20.WhoAmI()
L3GD20.Init()
while 1:
    #print "X:0x%04X Y:0x%04X Z:0x%04X" % (LIS3DH.X(),LIS3DH.Y(),LIS3DH.Z())
    print "X:%d Y:%d Z:%d" % (L3GD20.X(),L3GD20.Y(),L3GD20.Z())
    time.sleep(0.1)
"""
    x1=LIS3DH.X()
    y1=LIS3DH.Y()
    z1=LIS3DH.Z()
    time.sleep(0.1)
    x2=LIS3DH.X()
    y2=LIS3DH.Y()
    z2=LIS3DH.Z()
    time.sleep(0.1)
    print "X:%d Y:%d Z:%d" % (x1-x2,y1-y2,z1-z2)
"""
