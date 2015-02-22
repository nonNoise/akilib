#import mraa

import smbus
import time

I2C_ADDR = 0x5C

class AKI_I2C_LPS25H:
    def __init__(self):
        print "AKI_I2C_LPS25H"
        self.i2c = smbus.SMBus(1)
    def i2cReg(self,wr,addr=0x00,data=0x00):
        try:
            if(wr == "w"):
                return self.i2c.write_byte_data(I2C_ADDR,addr,data)
            elif(wr == "r"):
                return self.i2c.read_byte_data(I2C_ADDR,addr)
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
        mbar = p/4096
        return mbar

    def Temp (self):
        t = 0
        t = t | self.i2cReg("r",0x2B) <<0
        t = t | self.i2cReg("r",0x2C) <<8
        t = -((t-1)^0xffff)
        return (42.5+(t/480.0))