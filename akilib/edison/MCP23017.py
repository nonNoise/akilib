
############################################################
#The MIT License (MIT)
#Copyright (c) 2015 Yuta KItagami
#Project:    https://github.com/nonNoise/akilib
############################################################

import mraa
import time
from struct import *


I2C_PORT = 6
I2C_ADDR = 0x20

class MCP23017:

    def __init__(self):
        print "MCP23017 Open."
        i2c = mraa.I2c(I2C_PORT)
        i2c.address(I2C_ADDR)

    def i2cReg(self,wr,addr,data):
        if(wr == "w"):
            return i2c.writeReg(addr,data)
        elif(wr == "r"):
            return i2c.readReg(addr)
        else :
            return -1

    def IODIRA(self,wr,data):       
        return i2cReg(wr,0x00,data);
    def IPOLA(self,wr,data):        
        return i2cReg(wr,0x02,data);
    def GPINTENA(self,wr,data):     
        return i2cReg(wr,0x04,data);
    def DEFVALA(self,wr,data):      
        return i2cReg(wr,0x06,data);
    def INTCONA(self,wr,data):      
        return i2cReg(wr,0x08,data);
    def IOCONA(self,wr,data):       
        return i2cReg(wr,0x0A,data);
    def GPPUA(self,wr,data):        
        return i2cReg(wr,0x0C,data);
    def INTFA(self,wr,data):        
        return i2cReg(wr,0x0E,data);
    def INTCAPA(self,wr,data):      
        return i2cReg(wr,0x10,data);
    def GPIOA(self,wr,data):        
        return i2cReg(wr,0x12,data);
    def OLATA(self,wr,data):        
        return i2cReg(wr,0x14,data);

    def IODIRB(self,wr,data):       
        return i2cReg(wr,0x01,data);
    def IPOLB(self,wr,data):        
        return i2cReg(wr,0x03,data);
    def GPINTENB(self,wr,data):     
        return i2cReg(wr,0x05,data);
    def DEFVALB(self,wr,data):      
        return i2cReg(wr,0x07,data);
    def INTCONB(self,wr,data):      
        return i2cReg(wr,0x09,data);
    def IOCONA(self,wr,data):       
        return i2cReg(wr,0x0B,data);
    def GPPUB(self,wr,data):        
        return i2cReg(wr,0x0D,data);
    def INTFB(self,wr,data):        
        return i2cReg(wr,0x0F,data);
    def INTCAPB(self,wr,data):      
        return i2cReg(wr,0x11,data);
    def GPIOB(self,wr,data):        
        return i2cReg(wr,0x13,data);
    def OLATB(self,wr,data):        
        return i2cReg(wr,0x15,data);

