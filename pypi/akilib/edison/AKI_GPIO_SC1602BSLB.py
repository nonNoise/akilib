# -*- coding: utf-8 -*-

############################################################
#The MIT License (MIT)
#Copyright (c) 2015 Yuta KItagami
#Project:    https://github.com/nonNoise/akilib
############################################################

import time
import mraa


class AKI_GPIO_SC1602BSLB:
    def __init__(self,RS,E,D4,D5,D6,D7):
        self.RS = mraa.Gpio(RS)
        self.E = mraa.Gpio(E)
        self.D4 = mraa.Gpio(D4)
        self.D5 = mraa.Gpio(D5)
        self.D6 = mraa.Gpio(D6)
        self.D7 = mraa.Gpio(D7)       
        self.RS.dir(mraa.DIR_OUT)
        self.E.dir(mraa.DIR_OUT)
        self.D4.dir(mraa.DIR_OUT)
        self.D5.dir(mraa.DIR_OUT)
        self.D6.dir(mraa.DIR_OUT)
        self.D7.dir(mraa.DIR_OUT)

    def LCD_bitwrite(self,rs,data):   
        self.RS.write(rs)
        self.D7.write((data&0x08)>>3 )
        self.D6.write((data&0x04)>>2 )
        self.D5.write((data&0x02)>>1 )
        self.D4.write((data&0x01)>>0 )

        self.E.write(1)
        time.sleep(0.01)
        self.E.write(0)
        time.sleep(0.01)

        self.D7.write(0)
        self.D6.write(0)
        self.D5.write(0)
        self.D4.write(0)
        
    def LCD_Write(self,rs,data):   
        self.LCD_bitwrite(rs, (data&0xf0)>>4)
        self.LCD_bitwrite(rs, (data&0x0f))
        #time.sleep(0.1)


    def LCD_Init(self):
        self.LCD_bitwrite(0,0x03);
        time.sleep(0.1)
        self.LCD_bitwrite(0,0x03);
        time.sleep(0.1)
        self.LCD_bitwrite(0,0x03);
        time.sleep(0.1)
        self.LCD_bitwrite(0,0x02);
        time.sleep(0.1)
        rLCD_Display_Cmd = 0x08;
        
        self.LCD_Write(0,0x28);     #ファンクションセット　DL = 0; N = 1; F = 0;
        time.sleep(0.1)
        self.LCD_Write(0,0x0E);     #表示コントロール D = 0; C = 0; B = 0;
        time.sleep(0.1)
        self.LCD_Write(0,0x01);     #表示クリア
        time.sleep(0.1)
        self.LCD_Write(0,0x06);     #エントリーモードセット　l/D = 0; S = 0;
        time.sleep(0.1)
    def DisplayON(self):
        self.LCD_Write(0,0x0F);

    def ClearDisplay(self):
        # "Clear Display"
        self.LCD_Write(0,0x01);
        self.LCD_Write(0,0x02);

    def WritePos(self,Row,Col):        
        if(Row == 0) :
            Row = 0x00
        elif(Row == 1) :
            Row = 0x40
        elif(Row == 2) :
            Row = 0x14
        elif(Row == 3) :
            Row = 0x54

        if(Row == 2 or Row == 3 ) :
            Col = Col | 0x04
        self.LCD_Write( 0 , 0x80 | Col | Row);

    def WriteChar(self,c):
        self.LCD_Write(1,ord(c))

    def WriteStr(self,s,t=0):
        for c in s :        
            self.LCD_Write(1,ord(c))
            time.sleep(t)

    def NewClearDisplay(self,pos,time):
        self.WritePos(pos,0)
        self.WriteStr("                ",time)
        # "Clear Display"




