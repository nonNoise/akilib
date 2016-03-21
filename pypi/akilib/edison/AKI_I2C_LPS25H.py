
############################################################
#The MIT License (MIT)
#Copyright (c) 2015 Yuta KItagami
#Project:    https://github.com/nonNoise/akilib
############################################################

import mraa
import time
from struct import *

class AKI_I2C_LPS25H:
    def __init__(self,port):
        print "AKI_I2C_LPS25H"
        I2C_PORT = port
        self.I2C_ADDR = 0x5C
        self.i2c = mraa.I2c(I2C_PORT)
        self.i2c.address(self.I2C_ADDR)
    def i2cReg(self,wr,addr=0x00,data=0x00):
        try:
            if(wr == "w"):
                #print "W:0x%02X = 0x%02X" % (addr,data)
                return self.i2c.writeReg(addr,data)
            elif(wr == "r"):
                tmp = self.i2c.readReg(addr)
                #print "R:0x%02X = 0x%02X" % (addr,tmp)
                return tmp
            else :
                return -1
        except IOError, err:
            print "No ACK!"
            time.sleep(0.1)
            self.i2cReg(wr,addr,data)
    def WHO_AM_I(self):
        # "WHO_AM_I"
        return self.i2cReg("r",0x0F)

    def Init(self):
        return self.i2cReg("w",0x20,0x90) 
 
    def Press(self):
        p =0
        p = p | self.i2cReg("r",0x28) <<0
        p = p | self.i2cReg("r",0x29) <<8
        p = p | self.i2cReg("r",0x2A) <<16
        mbar = p/4096.00
        return mbar

    def Temp (self):
        t = 0
        t = t | self.i2cReg("r",0x2B) <<0
        t = t | self.i2cReg("r",0x2C) <<8
        t = -((t-1)^0xffff)
        return (42.5+(t/480.0))
