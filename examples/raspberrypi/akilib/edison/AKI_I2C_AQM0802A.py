
############################################################
#The MIT License (MIT)
#Copyright (c) 2015 Yuta KItagami
#Project:    https://github.com/nonNoise/akilib
############################################################

import mraa
import time

I2C_ADDR = 0x3E

class AKI_I2C_AQM0802A:
    def __init__(self):
        self.i2c = mraa.I2c(6)  
        self.i2c.frequency(100000)
        self.i2c.address(I2C_ADDR)
        #self.i2c.write(0xff)
    def Init_LCD(self):
        # "Function set"
        self.i2c.writeReg(0x00,0x38)
        time.sleep(0.1)
        # "Function set"
        self.i2c.writeReg(0x00,0x39)
        time.sleep(0.1)
        # "Internal OSC frequency "
        self.i2c.writeReg(0x00,0x14)
        time.sleep(0.1)
        # "Contrast set "
        self.i2c.writeReg(0x00,0x70)
        time.sleep(0.1)
        # "Power/ICON/Contrast control "
        self.i2c.writeReg(0x00,0x56)
        time.sleep(0.1)
        # "Follower control "
        self.i2c.writeReg(0x00,0x6C)
        time.sleep(0.1)

        time.sleep(0.20)
        # "Function set"
        self.i2c.writeReg(0x00,0x38)
        time.sleep(0.1)


        # "Clear Display"
        self.i2c.writeReg(0x00,0x01)
        time.sleep(0.20)
        # "Return Home"
        self.i2c.writeReg(0x00,0x02)
        time.sleep(0.002)
        # "Display ON!"
        self.i2c.writeReg(0x00,0x0C)
        time.sleep(0.002)
        # "Clear Display"
        self.i2c.writeReg(0x00,0x01)
        time.sleep(0.02)
        # "Light Display"
        #self.i2c.writeReg(0x00,0x2a)
        #time.sleep(0.1)
        #self.i2c.writeReg(0x00,0x79)
        #time.sleep(0.1)
        #self.i2c.writeReg(0x00,0xFF)
        #time.sleep(0.1)
        #self.i2c.writeReg(0x00,0x78)
        #time.sleep(0.1)
        #self.i2c.writeReg(0x00,0x28)
        #time.sleep(0.1)


    def ClearDisplay(self):
        # "Clear Display"
        self.i2c.writeReg(0x00,0x01)
        #time.sleep(0.1)

    def WritePos(self,a,b):     
        if a ==0:
            self.i2c.writeReg(0x00,0x80|b)
        elif a ==1:
            self.i2c.writeReg(0x00,0x80|0x40|b)
        #time.sleep(0.3)

    def WriteChar(self,c):
        self.i2c.writeReg(0x40,c )
        #time.sleep(0.3)

    def WriteStr(self,s):
        #print s
        for c in s :        
            #print ord(c)
            self.i2c.writeReg(0x40,ord(c))
            #time.sleep(0.3)

    def NewClearDisplay(self,pos,time):
        self.WritePos(pos,0)
        self.WriteStr("                ",time)
        # "Clear Display"




