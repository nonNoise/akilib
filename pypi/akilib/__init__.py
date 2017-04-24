############################################################
#The MIT License (MIT)
#Copyright (c) 2015 Yuta KItagami
#Project:    https://github.com/nonNoise/akilib
############################################################


import platform

plat = platform.platform()

#-----------------------------------------#
# Intel Edison platform
#-----------------------------------------#
if "edison" in plat :
    #print "Platform is Edison "
    from edison.test import test
    from edison.AKI_I2C_HDC1000 import AKI_I2C_HDC1000
    from edison.AKI_I2C_L3GD20 import AKI_I2C_L3GD20
    from edison.AKI_I2C_LPS25H import AKI_I2C_LPS25H
    from edison.AKI_I2C_LIS3DH import AKI_I2C_LIS3DH
    from edison.AKI_I2C_OLED import AKI_I2C_OLED
    from edison.AKI_I2C_MCP23017 import AKI_I2C_MCP23017
    from edison.AKI_I2C_SO1602AWYB import AKI_I2C_SO1602AWYB
    from edison.AKI_I2C_S11059 import AKI_I2C_S11059
    from edison.AKI_I2C_AQM0802A import AKI_I2C_AQM0802A
    from edison.AKI_SPI_AQM1248A import AKI_SPI_AQM1248A
    from edison.AKI_GPIO_SG12864ASLB import AKI_GPIO_SG12864ASLB

#-----------------------------------------#
# Raspberry Pi platform
#-----------------------------------------#
if  ("armv7l" or "armv6l")  in plat :
    #print "Platform is RaspberryPi "
    from raspberrypi.AKI_I2C_MCP3425 import AKI_I2C_MCP3425
    from raspberrypi.AKI_I2C_LPS25H import AKI_I2C_LPS25H
    from raspberrypi.AKI_I2C_HDC1000 import AKI_I2C_HDC1000
    from raspberrypi.AKI_I2C_AQM0802A import AKI_I2C_AQM0802A
    from raspberrypi.AKI_I2C_AQM1602A import AKI_I2C_AQM1602A
    from raspberrypi.AKI_I2C_ACM1602N1 import AKI_I2C_ACM1602N1
    from raspberrypi.AKI_I2C_ADT7410 import AKI_I2C_ADT7410
    #from raspberrypi.AKI_GPIO_SC1602BSLB import AKI_GPIO_SC1602BSLB
    from raspberrypi.AKI_I2C_S11059 import AKI_I2C_S11059
