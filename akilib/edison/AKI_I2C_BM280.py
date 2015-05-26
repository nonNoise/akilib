
############################################################
#The MIT License (MIT)
#Copyright (c) 2015 Yuta KItagami
#Project:    https://github.com/nonNoise/akilib
############################################################


import mraa
import time
from struct import *



class AKI_I2C_BM280:
    def __init__(self,addr):
        I2C_PORT = 6
        self.I2C_ADDR = addr
        self.i2c = mraa.I2c(I2C_PORT)
        self.i2c.address(self.I2C_ADDR)

    def i2cReg(self,wr,addr,data=0x00):
        if(wr == "w"):
            print "W:0x%02X = 0x%02X" % (addr,data)
            return self.i2c.writeReg(addr,data)
        elif(wr == "r"):
            #self.i2c.writeReg(addr,data)
            tmp = self.i2c.readReg(addr)
            print "R:0x%02X = 0x%02X" % (addr,tmp)
            return tmp
        else :
            return -1