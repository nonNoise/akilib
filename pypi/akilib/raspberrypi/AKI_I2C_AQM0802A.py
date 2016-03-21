import smbus
import time

I2C_ADDR = 0x3e
class AKI_I2C_AQM0802A:
    def __init__(self):
        print "AKI_I2C_AQM0802A"
        self.i2c = smbus.SMBus(1)
    def i2cReg(self,wr,addr,data):
        try:
            if(wr == "w"):
                return self.i2c.write_byte_data(I2C_ADDR,addr,data)
            elif(wr == "r"):
                return self.i2c.read_byte(I2C_ADDR,addr)
            else :
                return -1
        except IOError, err:
            print "No ACK!"
            exit()
    def Init_LCD(self):
        # "Function set"
        self.i2cReg("w",0x00,0x38)
        time.sleep(0.10)
        # "Function set"
        self.i2cReg("w",0x00,0x39)
        time.sleep(0.10)
        # "Internal OSC frequency"
        self.i2cReg("w",0x00,0x14)
        time.sleep(0.10)
        # "Contrast Set"
        self.i2cReg("w",0x00,0x70)
        time.sleep(0.10)
        # "Power/ICON Set"
        self.i2cReg("w",0x00,0x56)
        time.sleep(0.10)
        # "Follower control"
        self.i2cReg("w",0x00,0x6c)
        time.sleep(0.10)
        # "Function set"
        self.i2cReg("w",0x00,0x38)
        time.sleep(0.10)
        # "Display ON/OFF"
        self.i2cReg("w",0x00,0x0c)
        time.sleep(0.10)


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
	time.sleep(0.3)

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

