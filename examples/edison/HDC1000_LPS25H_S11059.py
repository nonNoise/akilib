# -*- encoding:utf8 -*-
from akilib import AKI_I2C_HDC1000
#akilibライブラリのAKI_I2C_HDC1000を使用することを宣言
from akilib import AKI_I2C_LPS25H
#akilibのAKI_I2C_LPS25Hを使用する事を宣言
from akilib import AKI_I2C_S11059
#akilibのAAKI_I2C_S11059を使用する事を宣言
import time
#timeライブラリ
import datetime


#================================================#
HDC1000 = AKI_I2C_HDC1000(1)
#HDC1000をI2C_1で使用する事を宣言
HDC1000.Config()
#HDC1000特有の初期化処理を行います。
#================================================#
LPS25H = AKI_I2C_LPS25H(1)
#LPS25HをI2C_1に接続していることを設定
LPS25H.Init()
#LPS25H特有の初期化を行います。
#================================================#
S11059 = AKI_I2C_S11059(1)
#S11059をI2C_1で使用する事を宣言
S11059.Init()
#S11059特有の初期化処理を行います。
#================================================#
while 1:
#無限ループ文 終了するときはキーボードでCtrl+Cを押します。
    d = datetime.datetime.today()
    print d.strftime("%Y-%m-%d %H:%M:%S")
    print "%d'C / %d /" % (HDC1000.Temperature(),HDC1000.Humidity())
    #温度を取得します。表記は℃
    #湿度を取得します。表記は％
    print "%d[hps] / %d'C" % (LPS25H.Press(),LPS25H.Temp())
    #気圧データを取得します。単位はhPa(ヘクトパスカル)
    #温度データを取得します。単位は℃
    print "R:0x%02X G:0x%02X B:0x%02X IR:0x%02X " % S11059.RGBISens()
    print "-" *20
    f = open("deta.csv","a")
    f.write("%s," % d.strftime("%Y/%m/%d"))
    f.write("%s," % d.strftime("%H:%M:%S"))
    f.write("%0.3f,%0.3f," % (HDC1000.Temperature(),HDC1000.Humidity()))
    f.write("%0.3f,%0.3f," % (LPS25H.Press(),LPS25H.Temp()))
    f.write("%d,%d,%d,%d" % S11059.RGBISens())
    f.write("\n")
    f.close()
    time.sleep(10)
