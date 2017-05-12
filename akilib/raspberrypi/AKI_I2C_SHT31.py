import smbus 
import time
from struct import *

class AKI_I2C_SHT31:
    def __init__(self):
        self.I2C_ADDR = 0x45
        self.i2c = smbus.SMBus(1)

    def i2cReg(self,wr,addr=0x00,data=0x0000,byte=0):
        try :
            if(wr == "w"):
                return self.i2c.write_i2c_block_data(self.I2C_ADDR, (data&0xFF00)>>8, [(data&0x00FF)])
            elif(wr == "r"):
                return self.i2c.read_i2c_block_data(self.I2C_ADDR, 0x00, byte) 
            else :
               return -1
        except IOError, err:
            print "No ACK!"
            time.sleep(0.1)
            self.i2cReg(wr,addr,data)
    def BussReset(self):
        self.i2c.write_byte(0x00,0x06)
        time.sleep(1)
        
    def SoftReset(self):
        self.i2cReg("w",data=0x30A2)
        time.sleep(1)
        self.i2cReg("w",data=0x3041)
        time.sleep(1)

            
    def Heater(self,onoff):
        if(onoff=="ON"):
            self.i2cReg("w",data=0x306D)
        else:
            self.i2cReg("w",data=0x3066)
    def ReadStatus(self):
        self.i2cReg("w",data=0xF32D)
        data = self.i2cReg("r",byte=3)
        return data



    def GetTempHum(self):
        try :
            self.i2cReg("w",data=0x2400)
            time.sleep(0.5)
            #self.i2cReg("w",data=0x2737)
            #time.sleep(0.1)
            data = self.i2cReg("r",byte=6)
            
            self.TMP = 0.0
            temp = data[1] | (data[0]<<8)
            self.TMP = ((temp * 175.0)/65535.0)-45
            self.HUM = 0.0
            hum = data[4] | (data[3]<<8)
            self.HUM = ((hum * 100.0)/65535.0)

            
        except IOError, err:
            print "No ACK!"
            time.sleep(0.1)
            self.GetTempHum()

    def Temperature(self):
        return self.TMP

    def Humidity(self):
        return self.HUM
