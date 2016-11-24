
############################################################
#The MIT License (MIT)
#Copyright (c) 2015 Yuta KItagami
#Project:    https://github.com/nonNoise/akilib
############################################################


import smbus
import time
from struct import *

class AKI_I2C_S11059:
    def __init__(self,I2C_PORT):
        self.I2C_ADDR = 0x2A
        self.i2c = smbus.SMBus(1)

    def i2cReg(self,wr,addr,data=0x00):
        if(wr == "w"):
            return  self.i2c.write_byte_data(self.I2C_ADDR,addr,data)
        elif(wr == "r"):
            return self.i2c.read_byte_data(self.I2C_ADDR,addr)
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
