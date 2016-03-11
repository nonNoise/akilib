
import time
from akilib.edison import AKI_I2C_LIS3DH
import math


LIS3DH = AKI_I2C_LIS3DH.AKI_I2C_LIS3DH(1)

time.sleep(0.01)
LIS3DH.WhoAmI()
LIS3DH.Init()

while 1:
    nowx = 0
    nowy = 0
    nowz = 0
    math.tan(1)
    for i in range(100):
        nowx = nowx + LIS3DH.X()
        nowy = nowy + LIS3DH.Y()
        nowz = nowz + LIS3DH.Z()
    nowx = nowx/100
    nowy = nowy/100
    nowz = nowz/100

    time.sleep(0.1)
    x = (LIS3DH.X()/65535)
    y = (LIS3DH.Y()/65535)
    z = (LIS3DH.Z()/65535)
    print "X:0x%04X Y:0x%04X Z:0x%04X" % (LIS3DH.X(),LIS3DH.Y(),LIS3DH.Z())
    print "X:%d Y:%d Z:%d" % (x,y,z)
    #print "X:%d Y:%d Z:%d" % (nowx,nowy,nowz)
    oldx = nowx
    oldy = nowy
    oldz = nowz

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
