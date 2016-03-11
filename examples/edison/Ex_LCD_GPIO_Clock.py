from akilib import AKI_GPIO_SC1602BSLB
import time
import datetime

LCD = AKI_GPIO_SC1602BSLB(33,47,48,36,20,14)

LCD.LCD_Init()
LCD.DisplayON()
LCD.ClearDisplay()

LCD.WritePos(0,0)
LCD.WriteStr("Wakeup NOW")
import ipget
p = ipget.ipget()
print p.ipaddr("wlan0")
LCD.WritePos(1,0)
LCD.WriteStr(p.ipaddr("wlan0"))
time.sleep(1.8)
LCD.NewClearDisplay(0,0)
LCD.NewClearDisplay(1,0)


LCD.WritePos(0,0)
LCD.WriteStr("Hello Edison.")
LCD.WritePos(1,0)
LCD.WriteStr("It's a NEW WORLD")
time.sleep(1.8)


while 1 :
        LCD.ClearDisplay()
        d = datetime.datetime.today()
        print d.strftime("%Y-%m-%d %H:%M:%S")
        LCD.WritePos(0,0)
        LCD.WriteStr(str(d.strftime("%m/%d")))
        LCD.WritePos(1,0)
        LCD.WriteStr(str(d.strftime("%H:%M:%S")))
        time.sleep(1.2)



