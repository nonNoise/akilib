
from akilib.raspberrypi import AKI_I2C_ADT7410
import time

adt7410 = AKI_I2C_ADT7410.AKI_I2C_ADT7410()
adt7410.Init()
print adt7410.read()
