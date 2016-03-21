import smbus 
import time
from struct import *


I2C_PORT = 6
I2C_ADDR = 0x40

class AKI_I2C_HDC1000:
    def __init__(self):
        print "== HDC1000 Open =="          
        print "* I2C Port:%d" % I2C_PORT     
        print "* I2C Addr:0x%2x" % I2C_ADDR     
        print "=" *20
        self.i2c = smbus.SMBus(1)

    def i2cReg(self,wr,addr=0x00,data=0x0000):
        try :
            if(wr == "w"):
                tmp = (data&0x00FF)<<8 | (data&0xFF00)>>8
                #print "W:0x%02X = 0x%04X" % (addr,data)
                return self.i2c.write_word_data(I2C_ADDR,addr,tmp)
            elif(wr == "r"):
                tmp =  self.i2c.read_word_data(I2C_ADDR,addr)
                tmp = (tmp&0x00FF)<<8 | (tmp&0xFF00)>>8               
                #print "R:0x%02X = 0x%04X" % (addr,tmp)
                return tmp
            else :
               return -1
        except IOError, err:
            print "No ACK!"
            time.sleep(0.1)
            self.i2cReg(wr,addr,data)
    def Config(self):
         # 0 - 7 bit = 0
         # 8bit :     HRES1 = 0
         # 9bit :     HRES2 = 0 14bit mode
         # 10bit :     TRES = 0
         # 11bit :     BTST = 0 (ReadOnly)
         # 12bit :     MODE = 0
         # 13bit :     Reserved = 0
         # 14bit :     Reserved = 0
         # 15bit :     RST = 0
         self.i2cReg('r',0xFE)
         self.i2cReg('r',0xFF)
         self.i2cReg('r',0x02)
         self.i2cReg('w',0x02,0x0000)
         self.i2cReg('r',0x02)
         time.sleep(0.01)
    def Temperature(self):
        try :
            self.i2c.write_byte(I2C_ADDR,0x00)
            time.sleep(0.20)
            d=[0]*2
            # print self.i2c.read_block_data(I2C_ADDR,0x00)
            d[0] = self.i2c.read_byte(I2C_ADDR) 
            time.sleep(0.001)
            d[1] = self.i2c.read_byte(I2C_ADDR) 
            time.sleep(0.001)
            #print "0x%02X :0x%02X" % (d[0],d[1])
            raw = ( d[0]<<8 | d[1] )
            #print (float(raw)/(2**16))*(165-40)
            return float(raw)/65536.0*165.0-40.0
        except IOError, err:
            print "No ACK!"
            time.sleep(0.1)
            self.Temperature()

    def Humidity(self):
        try :
            self.i2c.write_byte(I2C_ADDR,0x00)
            time.sleep(0.10)
            d=[0]*2
            d[0] = self.i2c.read_byte(I2C_ADDR) 
            time.sleep(0.001)
            d[1] = self.i2c.read_byte(I2C_ADDR) 
            time.sleep(0.001)
            #print "0x%02X :0x%02X" % (d[0],d[1])
            raw = ( d[0]<<8 | d[1] )
            return float(raw)/65536.0*100.0
        except IOError, err:
            print "No ACK!"
            time.sleep(0.1)
            self.Humidity()




    def LsbtoMsb(self,lsb,q):
         tmp = 0
         for i in range(q/2):
              tmp = tmp| ((lsb&(0x01<<i))>>i)<<(q-1-i)
         for i in range(q/2):
              tmp = tmp| ((lsb&(0x10<<i))>>i)>>(i+1)
         return tmp

