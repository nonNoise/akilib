
############################################################
#The MIT License (MIT)
#Copyright (c) 2015 Yuta KItagami
#Project:    https://github.com/nonNoise/akilib
############################################################


import mraa
import time
from struct import *

class AKI_SPI_AQM1248A:
    def __init__(self):
        self.RS = mraa.Gpio(36) #GP_IO14
        self.RS.dir(mraa.DIR_OUT)
        self.RS.write(1)

        self.CS = mraa.Gpio(48) #GP_IO15
        self.CS.dir(mraa.DIR_OUT)
        self.CS.write(1)

        self.SPI = mraa.Spi(5)
        self.SPI.frequency(20000)
        print "Init"
        try:
            from PIL import Image, ImageDraw

            SCREEN_WIDTH = 128
            SCREEN_HEIGHT = 48
            self.buffer = Image.new("1", (SCREEN_WIDTH,SCREEN_HEIGHT), "black") #"white"
            self.draw = ImageDraw.Draw(self.buffer)
        except ImportError:
            raise NoSuchLibraryError('PIL')


    def Write_Command(self,data):
        self.CS.write(0)
        self.RS.write(0)
        self.SPI.write(pack('B',data));
        self.CS.write(1)
        self.RS.write(1)
        #time.sleep(0.02)
        #print "Command"
    def Write_Data(self,data):
        self.CS.write(0)
        self.RS.write(1)
        self.SPI.write(pack("B",data));
        self.CS.write(1)
        self.RS.write(1)
        #time.sleep(0.0002)
        #print "Data"
    def SetUp(self):
        self.Write_Command(0xAE)
        self.Write_Command(0xA0)
        self.Write_Command(0xC8)
        self.Write_Command(0xA3)
        self.Write_Command(0x2C)
        time.sleep(0.002)
        self.Write_Command(0x2E)
        time.sleep(0.002)
        self.Write_Command(0x2F)
        time.sleep(0.002)
        self.Write_Command(0x23)
        self.Write_Command(0x81)
        self.Write_Command(0x1C)
        self.Write_Command(0xA4)
        self.Write_Command(0x40)
        self.Write_Command(0xA6)
        self.Write_Command(0xAF)
    def Page(self,page):
        self.Write_Command( 0xB0 | (page & 0x0F))
    def Column(self,col):
        self.Write_Command(0x10 | ((col >> 4) & 0x0F))
        self.Write_Command(0x00 | (col & 0x0F))
    def Line(self,line):
        self.Write_Command(0x40 | (line & 0x0F))
    
    def Clear(self):
        for i in range(8+1):
            self.Page(i)
            self.Column(0)
            for j in range(128):
                self.Write_Data(0)
    
    def Test(self):
        for i in range(6):
            self.Page(i)
            self.Column(0)
            for j in range(128):
                self.Write_Data(0x80)
    def Pixel_Check(self,x,y):
        if(self.buffer.getpixel((x,y)) > 127):
            return 1
        else :
            return 0

    def Uplode(self):
        for i in range(6):
            self.Page(i)
            self.Column(0)
            for j in range(128):
                #print i,j,((0+(8*i))<<0)
                data = 0
                data = data | self.Pixel_Check(j,(0+(8*i)))<<0
                data = data | self.Pixel_Check(j,(1+(8*i)))<<1
                data = data | self.Pixel_Check(j,(2+(8*i)))<<2
                data = data | self.Pixel_Check(j,(3+(8*i)))<<3
                data = data | self.Pixel_Check(j,(4+(8*i)))<<4
                data = data | self.Pixel_Check(j,(5+(8*i)))<<5
                data = data | self.Pixel_Check(j,(6+(8*i)))<<6
                data = data | self.Pixel_Check(j,(7+(8*i)))<<7
                self.Write_Data(data)   
                #print data ,
            #print ""
        #self.buffer.save("img.png", "PNG")     



