# -*- coding: utf-8 -*-
#ライブラリの宣言
from akilib import AKI_I2C_AQM0802A
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) #GPIOの使用を宣言
GPIO.setup(4,GPIO.OUT)  #BackLight用の端子
GPIO.setup(17,GPIO.OUT) #Reset用の端子

GPIO.output(17,0) # 起動時にリセットします。 
time.sleep(0.1)	# 0.1秒リセット
GPIO.output(17,1) # リセット解除

lcd = AKI_I2C_AQM0802A() #AQM0802A用のオブジェクトを参照
lcd.Init_LCD()	#LCDの初期化
lcd.ClearDisplay() #LCDの表示クリア

GPIO.output(4,1) #BackLight ON!
time.sleep(0.1)

while 1:
	lcd.ClearDisplay() #LCDの表示クリア
	time.sleep(1)
	lcd.WritePos(0,0) 　　　　#0列0行から表示開始
	lcd.WriteStr("Hello")　　#表示文字を記述
	lcd.WritePos(1,1) 　　　　#1列1行から表示開始
	lcd.WriteStr("World!")　　#表示文字を記述

	time.sleep(1)

	lcd.ClearDisplay()
	time.sleep(1)
	lcd.WritePos(0,0)
	lcd.WriteStr("Hello",t=0.1)　　#0.1秒ごとに１文字を表示
	lcd.WritePos(1,1)
	lcd.WriteStr("World!",t=0.1)　　#0.1秒ごとに１文字を表示

	time.sleep(1)
