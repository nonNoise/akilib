# -*- coding: utf-8 -*-

############################################################
#The MIT License (MIT)
#Copyright (c) 2015 Yuta KItagami
#Project:    https://github.com/nonNoise/akilib
############################################################

import time
import RPi.GPIO as GPIO

class AKI_SC1602BSLB:
    def __init__(self,RS,E,D4,D5,D6,D7):
        self.RS = RS
        self.E = E
        self.D4 = D4
        self.D5 = D5
        self.D6 = D6
        self.D7 = D7
        GPIO.setwarnings(False) 
        GPIO.setmode( GPIO.BCM )
        GPIO.setup(self.RS, GPIO.OUT)
        GPIO.setup(self.E, GPIO.OUT)
        GPIO.setup(self.D4, GPIO.OUT)
        GPIO.setup(self.D5, GPIO.OUT)
        GPIO.setup(self.D6, GPIO.OUT)
        GPIO.setup(self.D7, GPIO.OUT)
    def LCD_bitwrite(self,rs,data):   
        GPIO.output(self.RS, rs)
        GPIO.output(self.D7, (data&0x08)>>3 )
        GPIO.output(self.D6, (data&0x04)>>2 )
        GPIO.output(self.D5, (data&0x02)>>1 )
        GPIO.output(self.D4, (data&0x01)>>0 )

        GPIO.output(self.E, 1)
        time.sleep(0.01)
        GPIO.output(self.E, 0)
        time.sleep(0.01)

        GPIO.output(self.D7,0)
        GPIO.output(self.D6,0)
        GPIO.output(self.D5,0)
        GPIO.output(self.D4,0)
        
    def LCD_Write(self,rs,data):   
        self.LCD_bitwrite(rs, (data&0xf0)>>4)
        self.LCD_bitwrite(rs, (data&0x0f))
        time.sleep(0.1)


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




