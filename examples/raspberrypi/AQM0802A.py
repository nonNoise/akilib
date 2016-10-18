from akilib.raspberrypi import AKI_I2C_AQM0802A
import time
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.OUT)

lcd = AKI_I2C_AQM0802A.AKI_I2C_AQM0802A()
lcd.Init_LCD()
lcd.ClearDisplay()
lcd.WritePos(0,0)

print "LCD Testing ....."
for i in range(0,10):
	GPIO.setup(4,GPIO.OUT)
	time.sleep(0.01)
	lcd.ClearDisplay()
	lcd.WritePos(0,0)
	lcd.WriteStr("Hello")
	GPIO.output(4,1)
	lcd.WritePos(1,0)
	lcd.WriteStr(str(i))
	time.sleep(0.5)
	print i
	GPIO.output(4,0)
	time.sleep(0.5)
lcd.ClearDisplay()
lcd.WritePos(0,0)
lcd.WriteStr("OK!!")
GPIO.output(4,0)
