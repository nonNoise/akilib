from akilib.raspberrypi import AKI_I2C_AQM0802A
import time



lcd = AKI_I2C_AQM0802A.AKI_I2C_AQM0802A()
lcd.Init_LCD()
lcd.ClearDisplay()
lcd.WritePos(0,0)

print "LCD Testing ....."
for i in range(0,10):
	lcd.ClearDisplay()
	lcd.WritePos(0,0)
	lcd.WriteStr("Hello")

	lcd.WritePos(1,0)
	lcd.WriteStr(str(i))
	time.sleep(0.7)
	print i

lcd.ClearDisplay()
lcd.WritePos(0,0)
lcd.WriteStr("OK!!")
