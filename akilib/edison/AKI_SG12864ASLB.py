
############################################################
#The MIT License (MIT)
#Copyright (c) 2015 Yuta KItagami
#Project:    https://github.com/nonNoise/akilib
############################################################

import mraa
import time
from struct import *



class AKI_SG12864ASLB:
    def __init__(self):
        self.HI = 0     # NOT LogicIC
        self.LOW = 1    # NOT LogicIC

        self.DI = mraa.Gpio(21) #GP_IO183
        self.RW = mraa.Gpio(0) #GP_IO182
        self.E = mraa.Gpio(14) #GP_IO13
        self.DB0 = mraa.Gpio(20) #GP_IO12
        self.DB1 = mraa.Gpio(36) #GP_IO14
        self.DB2 = mraa.Gpio(48) #GP_IO15
        self.DB3 = mraa.Gpio(47) #GP_IO49
        self.DB4 = mraa.Gpio(33) #GP_IO48
        self.DB5 = mraa.Gpio(46) #GP_IO47
        self.DB6 = mraa.Gpio(32) #GP_IO46
        self.DB7 = mraa.Gpio(45) #GP_IO45
        self.CS1 = mraa.Gpio(15) #GP_IO165
        self.CS2 = mraa.Gpio(31) #GP_IO44
        self.DI.dir(mraa.DIR_OUT)
        self.RW.dir(mraa.DIR_OUT)
        self.E.dir(mraa.DIR_OUT)
        self.DB0.dir(mraa.DIR_OUT)
        self.DB1.dir(mraa.DIR_OUT)
        self.DB2.dir(mraa.DIR_OUT)
        self.DB3.dir(mraa.DIR_OUT)
        self.DB4.dir(mraa.DIR_OUT)
        self.DB5.dir(mraa.DIR_OUT)
        self.DB6.dir(mraa.DIR_OUT)
        self.DB7.dir(mraa.DIR_OUT)
        self.CS1.dir(mraa.DIR_OUT)
        self.CS2.dir(mraa.DIR_OUT)

        self.DI.write(self.LOW)
        self.RW.write(self.LOW)
        self.E.write(self.LOW)
        self.DB0.write(self.LOW)
        self.DB1.write(self.LOW)
        self.DB2.write(self.LOW)
        self.DB3.write(self.LOW)
        self.DB4.write(self.LOW)
        self.DB5.write(self.LOW)
        self.DB6.write(self.LOW)
        self.DB7.write(self.LOW)
        self.CS1.write(self.LOW)
        self.CS2.write(self.LOW)
        #time.sleep(0.01)
        self.RW.write(self.HI)
        #time.sleep(0.01)   

        print "Init"
        try:
            from PIL import Image, ImageDraw

            SCREEN_WIDTH = 128
            SCREEN_HEIGHT = 64
            self.buffer = Image.new("1", (SCREEN_WIDTH,SCREEN_HEIGHT), "black") #"white"
            self.draw = ImageDraw.Draw(self.buffer)
        except ImportError:
            raise NoSuchLibraryError('PIL')

    def Write_Command(self,data,cs):
        data = ~ data   # NOT LogicIC
        self.DI.write(self.LOW)
        #self.RW.write(self.HI)
        self.DB0.write((data&0x01)>>0)
        self.DB1.write((data&0x02)>>1)
        self.DB2.write((data&0x04)>>2)
        self.DB3.write((data&0x08)>>3)
        self.DB4.write((data&0x10)>>4)
        self.DB5.write((data&0x20)>>5)
        self.DB6.write((data&0x40)>>6)
        self.DB7.write((data&0x80)>>7)
        if (cs == 0):
            self.CS1.write(self.HI)
            self.CS2.write(self.LOW)
        else :
            self.CS1.write(self.LOW)
            self.CS2.write(self.HI)
        self.E.write(self.LOW)
        self.E.write(self.HI)
        self.E.write(self.LOW)
        #time.sleep(0.0001)     
        

    def Write_Data(self,data,cs):
        data = ~ data   # NOT LogicIC
        self.DI.write(self.HI)
        #self.RW.write(self.LOW)
        self.E.write(self.LOW)
        self.DB0.write((data&0x01)>>0)
        self.DB1.write((data&0x02)>>1)
        self.DB2.write((data&0x04)>>2)
        self.DB3.write((data&0x08)>>3)
        self.DB4.write((data&0x10)>>4)
        self.DB5.write((data&0x20)>>5)
        self.DB6.write((data&0x40)>>6)
        self.DB7.write((data&0x80)>>7)
        if (cs == 0):
            self.CS1.write(self.HI)
            self.CS2.write(self.LOW)
        else :
            self.CS1.write(self.LOW)
            self.CS2.write(self.HI)
        self.E.write(self.LOW)
        self.E.write(self.HI)
        self.E.write(self.LOW)
        #time.sleep(0.0001)     
        
    def SetUp(self):
        self.Write_Command(0xC0,0)
        self.Write_Command(0x3F,0)
        self.Write_Command(0xC0,1)
        self.Write_Command(0x3F,1)

    def SetPosData(self,x,y,deta):
        if( x < 64 ):
            self.Write_Command(0x40 | (x & 0x3F),0)
            self.Write_Command(0xB8 | (y & 0x07),0)
            self.Write_Data(deta,0)
        else    :
            self.Write_Command(0x40 | (x & 0x3F),1)
            self.Write_Command(0xB8 | (y & 0x07),1)
            self.Write_Data(deta,1)

    def Clear(self):
        for y in range(8):
            for x in range(128):
                self.SetPosData(x,y,0x00)

    def Test(self):
        for y in range(8):
            for x in range(128):
                self.SetPosData(x,y,0x0F)

    def Pixel_Check(self,x,y):
        if(self.buffer.getpixel((x,y)) > 127):
            return 1
        else :
            return 0

    def Uplode(self):
        for y in range(8):
            for x in range(128):
                #print i,j,((0+(8*i))<<0)
                data = 0
                data = data | self.Pixel_Check(x,(0+(8*y)))<<0
                data = data | self.Pixel_Check(x,(1+(8*y)))<<1
                data = data | self.Pixel_Check(x,(2+(8*y)))<<2
                data = data | self.Pixel_Check(x,(3+(8*y)))<<3
                data = data | self.Pixel_Check(x,(4+(8*y)))<<4
                data = data | self.Pixel_Check(x,(5+(8*y)))<<5
                data = data | self.Pixel_Check(x,(6+(8*y)))<<6
                data = data | self.Pixel_Check(x,(7+(8*y)))<<7
                self.SetPosData(x,y,data)
                #print data ,
            #print ""
        self.buffer.save("img.png", "PNG")      





