
from akilib.raspberrypi import AKI_I2C_HDC1000
import time

hdc = AKI_I2C_HDC1000.AKI_I2C_HDC1000()
hdc.Config()

while 1:
        print u'%02d C' % hdc.Temperature()
        print u'%02d %%' % hdc.Humidity()
        print u"-" * 20
        time.sleep(1)
