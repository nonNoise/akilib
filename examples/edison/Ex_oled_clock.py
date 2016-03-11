
#from akilib import AKI_I2C_OLED
from akilib import AKI_I2C_OLED
import ipget
import datetime
import time

oled = AKI_I2C_OLED()
oled.Init_OLED()

oled.WritePos(0,0)
oled.WriteStr("Hello Master.")
oled.ClearDisplay()
while 1 :
	d = datetime.datetime.today()
	ip = ipget.ipget()
	print d.strftime("%Y-%m-%d %H:%M:%S")
	oled.WritePos(0,0)
	oled.WriteStr(str(d.strftime("%Y-%m-%d")),1)
	oled.WritePos(1,3)
	oled.WriteStr(str(d.strftime("%H:%M:%S")),1)
	time.sleep(0.8)

