#import mraa

import smbus
import time

I2C_ADDR = 0x68

class AKI_I2C_MCP3425:

    def __init__(self,i2caddr):
        print "AKI_I2C_MCP3425"
        self.i2c = smbus.SMBus(1)

    def i2cReg(self,wr,addr=0x00,data=0x00):
        try:
            if(wr == "w"):
                #time.sleep(0.1)
                #print "W:0x%02X = 0x%04X" % (addr,data)
                #return self.i2c.writeReg(addr,data)
                return self.i2c.write_byte(I2C_ADDR,data)
            elif(wr == "r"):
                #return self.i2c.readReg(addr)
                ad1 = self.i2c.read_word_data(I2C_ADDR,addr)
                time.sleep(0.1)
                #print "0x%04X" % (ad1)
                return (ad1)

            else :
                return -1
        except IOError, err:
            print "No ACK!"
            time.sleep(0.1)
            self.i2cReg(wr,addr,data)
            
##########################################################################

    def AD_Init(self):
        print "Init"
        return self.i2cReg("w",0x00,0x80)
    def AD_Read(self):
        ad = 0.00001
        #self.i2cReg("w",0x00,0x80)
        ad = self.i2cReg("r",0x88)
        ad = ((ad&0x00ff)<<8) | ((ad&0xff00)>>8)
        #print "0x%04X " % ad

        if(ad & 0x8000 == 0x8000):
            return float(-((ad-1)^0xFFFF)) * 0.0625
        else :
            return float(ad) * 0.001 * 0.0625
