############################################################
#The MIT License (MIT)
#Copyright (c) 2015 Yuta KItagami
#Project:    https://github.com/nonNoise/akilib
############################################################

import mraa
import time
from struct import *


class AKI_I2C_SO1602AWYB:
    def __init__(self,port):
        I2C_PORT = port
        I2C_ADDR = 0x3C
        self.i2c = mraa.I2c(I2C_PORT)  
        self.i2c.address(I2C_ADDR)
    
    def Init_OLED(self):
        # "Clear Display"
        self.i2c.writeReg(0x00,0x01)
        time.sleep(0.20)
        # "Return Home"
        self.i2c.writeReg(0x00,0x02)
        time.sleep(0.002)
        # "Display ON!"
        self.i2c.writeReg(0x00,0x0F)
        time.sleep(0.002)
        # "Clear Display"
        self.i2c.writeReg(0x00,0x01)
        time.sleep(0.02)
        # "Light Display"
        self.i2c.writeReg(0x00,0x2a)
        self.i2c.writeReg(0x00,0x79)
        self.i2c.writeReg(0x00,0xFF)
        self.i2c.writeReg(0x00,0x78)
        self.i2c.writeReg(0x00,0x28)


    def ClearDisplay(self):
        # "Clear Display"
        self.i2c.writeReg(0x00,0x01)

    def WritePos(self,a,b):     
        if a ==0:
            self.i2c.writeReg(0x00,0x80|b)
        elif a ==1:
            self.i2c.writeReg(0x00,0x80|0x20|b)

    def WriteChar(self,c,t=20):
        self.i2c.writeReg(0x40,c )
        time.sleep(t/100.0)

    def WriteStr(self,s,t=20):
        #print s
        for c in s :        
            #print ord(c)
            self.i2c.writeReg(0x40,ord(c))
            time.sleep(t/100.0)

    def NewClearDisplay(self,pos,time):
        self.WritePos(pos,0)
        self.WriteStr("                ",time)
        # "Clear Display"




