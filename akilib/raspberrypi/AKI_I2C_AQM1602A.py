#import mraa

import smbus
import time

I2C_ADDR = 0x3E

class AKI_I2C_AQM1602A:
    def __init__(self):
        print "AKI_I2C_AQM1602A"
        self.i2c = smbus.SMBus(1)
    def i2cReg(self,wr,addr,data):
        try:
            if(wr == "w"):
                #time.sleep(0.1)
                #print "W:0x%02X = 0x%04X" % (addr,data)
                #return self.i2c.writeReg(addr,data)
                return self.i2c.write_byte_data(I2C_ADDR,addr,data)
            elif(wr == "r"):
                #return self.i2c.readReg(addr)
                return self.i2c.read_byte(I2C_ADDR,addr)
            else :
                return -1
        except IOError, err:
            print "No ACK!"
            #time.sleep(0.1)
            #self.i2cReg(wr,addr,data)
    def Init_LCD(self):
        # "Function set"
        self.i2cReg("w",0x00,0x38)
        time.sleep(0.1)
        # "Function set"
        self.i2cReg("w",0x00,0x39)
        time.sleep(0.1)
        # "Internal OSC frequency "
        self.i2cReg("w",0x00,0x14)
        time.sleep(0.1)
        # "Contrast set "
        self.i2cReg("w",0x00,0x7E)
        time.sleep(0.1)
        # "Power/ICON/Contrast control "
        self.i2cReg("w",0x00,0x54)
        time.sleep(0.1)
        # "Follower control "
        self.i2cReg("w",0x00,0x6C)
        time.sleep(0.1)

        time.sleep(0.50)
        # "Function set"
        self.i2cReg("w",0x00,0x38)
        time.sleep(0.1)


        # "Clear Display"
        self.i2cReg("w",0x00,0x01)
        time.sleep(0.20)
        # "Display ON!"
        self.i2cReg("w",0x00,0x0C)
        time.sleep(1)

    def ClearDisplay(self):
        # "Clear Display"
        self.i2cReg("w",0x00,0x01)
        #time.sleep(0.1)

    def WritePos(self,a,b):        
        if a ==0:
            self.i2cReg("w",0x00,0x80|b)
        elif a ==1:
            self.i2cReg("w",0x00,0x80|0x40|b)
        #time.sleep(0.3)

    def WriteChar(self,c):
        self.i2cReg("w",0x40,c )

    def WriteStr(self,s,t=0):
        #print s
        for c in s :        
            #print ord(c)
            self.i2cReg("w",0x40,ord(c))
            time.sleep(t)

    def NewClearDisplay(self,pos,time):
        self.WritePos(pos,0)
        self.WriteStr("                ",time)
        # "Clear Display"




