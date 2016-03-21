import smbus
import time

I2C_ADDR = 0x48

class AKI_I2C_ADT7410:
    def __init__(self):
        print "AKI_I2C_ADT7410"
        self.i2c = smbus.SMBus(1)
    def Init(self):
    	conf_data = self.i2c.read_byte_data(I2C_ADDR,0x03)
    	conf_data |= 0x80 | 0x60
    	self.i2c.write_byte_data(I2C_ADDR,0x03,conf_data)
    def read(self):
    	self.i2c.write_byte_data(I2C_ADDR,0x03,0x80|0x20)
    	time.sleep(0.2)
    	reg = self.i2c.read_i2c_block_data(I2C_ADDR,0x00,2)
    	temp = ((reg[0]&0x7F)<<8)|reg[1]
    	if(reg[0]&0x80) != 0:
    		temp -=65536
    	return (temp/128.0)
   
