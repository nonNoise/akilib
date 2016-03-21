
############################################################
#The MIT License (MIT)
#Copyright (c) 2015 Yuta KItagami
#Project:    https://github.com/nonNoise/akilib
############################################################


import mraa
import time
from struct import *

class AKI_I2C_HDC1000:
    def __init__(self,port):
        print "== HDC1000 Open =="      
        I2C_PORT = port
        self.i2c = mraa.I2c(I2C_PORT)
        I2C_ADDR = 0x40
        self.i2c.address(I2C_ADDR)

    def i2cReg(self,wr,addr,data=0x0000):
        if(wr == "w"):
            tmp = (data&0x00FF)<<8 | (data&0xFF00)>>8
            print "W:0x%02X = 0x%04X" % (addr,data)
            return self.i2c.writeWordReg(addr,tmp)
        elif(wr == "r"):
            tmp = self.i2c.readWordReg(addr)
            tmp = (tmp&0x00FF)<<8 | (tmp&0xFF00)>>8         
            print "R:0x%02X = 0x%04X" % (addr,tmp)
            return tmp
        else :
            return -1

    def Config(self):
        # 0 - 7 bit = 0
        # 8bit :    HRES1 = 0
        # 9bit :    HRES2 = 0 14bit mode
        # 10bit :   TRES = 0
        # 11bit :   BTST = 0 (ReadOnly)
        # 12bit :   MODE = 0
        # 13bit :   Reserved = 0
        # 14bit :   Reserved = 0
        # 15bit :   RST = 0
        self.i2cReg('r',0xFE)
        self.i2cReg('r',0xFF)
        self.i2cReg('r',0x02)
        self.i2cReg('w',0x02,0x0000)
        self.i2cReg('r',0x02)
        time.sleep(0.01)

    def Temperature(self):
        self.i2c.writeByte(0x00)
        time.sleep(0.05)
        d = self.i2c.read(2)
        #print "0x%02X :0x%02X" % (d[0],d[1])

        raw = ( d[0]<<8 | d[1] )
        #print (float(raw)/(2**16))*(165-40)
                
        return float(raw)/65536.0*165.0-40.0
    def Humidity(self):
        self.i2c.writeByte(0x00)
        time.sleep(0.05)
        d = self.i2c.read(2)
        #print "0x%02X :0x%02X" % (d[0],d[1])

        raw = ( d[0]<<8 | d[1] )

        return float(raw)/65536.0*100.0
    def LebtoMsb(self,lsb,q):
        tmp = 0
        for i in range(q/2):
            tmp = tmp| ((lsb&(0x01<<i))>>i)<<(q-1-i)
        for i in range(q/2):
            tmp = tmp| ((lsb&(0x10<<i))>>i)>>(i+1)
        return tmp

