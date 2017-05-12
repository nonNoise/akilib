#import mraa

import smbus
import time

I2C_ADDR = 0x40

MODE1              = 0x00
MODE2              = 0x01
SUBADR1            = 0x02
SUBADR2            = 0x03
SUBADR3            = 0x04
PRESCALE           = 0xFE
LED0_ON_L          = 0x06
LED0_ON_H          = 0x07
LED0_OFF_L         = 0x08
LED0_OFF_H         = 0x09
ALL_LED_ON_L       = 0xFA
ALL_LED_ON_H       = 0xFB
ALL_LED_OFF_L      = 0xFC
ALL_LED_OFF_H      = 0xFD

RESTART            = 0x80
SLEEP              = 0x10
ALLCALL            = 0x01
INVRT              = 0x10
OUTDRV             = 0x04


class AKI_I2C_PCA9685:
    def __init__(self,i2caddr):
        print "AKI_I2C_PCA9685"
        self.i2c = smbus.SMBus(1)

    def i2cReg(self,wr,addr=0x00,data=0x00):
        try:
            if(wr == "w"):
                return self.i2c.write_word_data(I2C_ADDR,addr,data)
            elif(wr == "r"):
                return self.i2c.read_word_data(I2C_ADDR,addr)
            else :
                return -1
        except IOError, err:
            print "No ACK!"
            time.sleep(0.1)
            self.i2cReg(wr,addr,data)

##########################################################################

    def SoftReset(self):
        self.i2c.write_byte(0x00,0x06)  #SWRST

    def PWM_Freq_Set(self,hz):
        prescaleval = 25000000.0    # 25MHz
        prescaleval /= 4096.0       # 12-bit
        prescaleval /= float(freq_hz)
        prescaleval -= 1.0
        prescale = int(math.floor(prescaleval + 0.5))

        old = self.i2cReg("r",MODE1);
        print "0x%02X" % old 
        new = (old & 0x7F) | 0x10    # sleep
        self.i2cReg("w",MODE1, new)  # go to sleep
        self.i2cReg("w",PRESCALE, prescale)
        self.i2cReg("w",MODE1, old)
        time.sleep(0.005)
        self.i2cReg("w",MODE1, old | 0x80)
