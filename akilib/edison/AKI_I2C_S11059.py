
############################################################
#The MIT License (MIT)
#Copyright (c) 2015 Yuta KItagami
#Project:    https://github.com/nonNoise/akilib
############################################################


import mraa
import time
from struct import *



class AKI_I2C_S11059:
    def __init__(self,port):
        self.I2C_ADDR = 0x2A
        self.i2c = mraa.I2c(port)
        self.i2c.address(self.I2C_ADDR)

    def i2cReg(self,wr,addr,data=0x00):
        if(wr == "w"):
            #print "W:0x%02X = 0x%02X" % (addr,data)
            return self.i2c.writeReg(addr,data)
        elif(wr == "r"):
            #self.i2c.writeReg(addr,data)
            tmp = self.i2c.readReg(addr)
            #print "R:0x%02X = 0x%02X" % (addr,tmp)
            return tmp
        else :
            return -1
    def Init(self):
        #-- Init --#
        self.i2cReg("w",0x00,0x89)
        self.i2cReg("w",0x00,0x09)
    def RED(self):
        return self.i2cReg("r",0x03)<<8 | self.i2cReg("r",0x04)
    def GREEN(self):
        return self.i2cReg("r",0x05)<<8 | self.i2cReg("r",0x06)
    def BLUE(self):
        return self.i2cReg("r",0x07)<<8 | self.i2cReg("r",0x08)
    def IR(self):
        return self.i2cReg("r",0x09)<<8 | self.i2cReg("r",0x0A)

    def RGBISens(self):
        #-- Red Color --#
        r = self.i2cReg("r",0x03)<<8 | self.i2cReg("r",0x04)
        #-- Green Color --#
        g = self.i2cReg("r",0x05)<<8 | self.i2cReg("r",0x06)
        #-- Blue Color --#
        b = self.i2cReg("r",0x07)<<8 | self.i2cReg("r",0x08)
        #-- Ir Data --#
        ir = self.i2cReg("r",0x09)<<8 | self.i2cReg("r",0x0A)
        return (r,g,b,ir)




