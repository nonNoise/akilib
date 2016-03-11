############################################################
#The MIT License (MIT)
#Copyright (c) 2015 Yuta KItagami
#Project:    https://github.com/nonNoise/akilib
############################################################


import mraa
import time
from struct import *

class AKI_I2C_LIS3DH:
    def __init__(self,port):
        I2C_PORT = port
        self.I2C_ADDR = 0x19
        self.i2c = mraa.I2c(I2C_PORT)
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
    def WhoAmI(self):
        print "Who am I?: 0x%02X" % self.i2cReg("r",0x0F)
        
    def Init(self):
        #-- Init --#
        self.i2cReg("w",0x20,0x7F)<<8
    def X(self):
        return  self.i2cReg("r",0x28)
    def Y(self):
        return (self.i2cReg("r",0x2B)<<8 | self.i2cReg("r",0x2A))
    def Z(self):
        return (self.i2cReg("r",0x2D)<<8 | self.i2cReg("r",0x2C))
