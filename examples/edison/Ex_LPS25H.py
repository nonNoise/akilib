
import time
from akilib.edison import AKI_I2C_LPS25H


LPS25H = AKI_I2C_LPS25H.AKI_I2C_LPS25H(1)

LPS25H.Init()
time.sleep(0.01)

while 1:
    #print "T:0x%04X P:0x%04X " % (LPS25H.Press(),LPS25H.Temp())
    print "P:%d T:%d " % (LPS25H.Press(),LPS25H.Temp())
    time.sleep(0.1)

