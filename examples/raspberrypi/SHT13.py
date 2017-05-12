import AKI_I2C_SHT31
import time

SHT31 = AKI_I2C_SHT31.AKI_I2C_SHT31()
SHT31.I2C_ADDR = 0x44
SHT31.SoftReset()
time.sleep(1)
print SHT31.ReadStatus()

while 1:
	print "-" *10
	print "%f %%" % SHT31.Humidity()
 	print "%f 'C" % SHT31.Temperature()
	time.sleep(1)
