from akilib import AKI_I2C_SHT31
from akilib import AKI_I2C_AQM0802A
import time

i2c = AKI_I2C_SHT31()
i2c.I2C_ADDR = 0x44
i2c.BussReset()
i2c.SoftReset()
print i2c.ReadStatus()

lcd = AKI_I2C_AQM0802A()
lcd.Init_LCD()
lcd.ClearDisplay()
lcd.WritePos(0,0)
lcd.WriteStr("Hello")

while 1:
	i2c.GetTempHum()
	print "-" *10
	print "%f %%" % i2c.Humidity()
 	print "%f 'C" % i2c.Temperature()
	time.sleep(0.1)
	lcd.ClearDisplay()
	lcd.WritePos(0,0)
	lcd.WriteStr("%0.2f %%" % i2c.Humidity() )
	lcd.WritePos(1,0)
	lcd.WriteStr("%0.2f C"  % i2c.Temperature() )

