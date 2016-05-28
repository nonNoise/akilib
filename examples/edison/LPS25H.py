# -*- encoding:utf8 -*-
from akilib import AKI_I2C_LPS25H
#akilibのAKI_I2C_LPS25Hを使用する事を宣言
import time 
#timeライブラリを使用する事を宣言
LPS25H = AKI_I2C_LPS25H(1)
#LPS25HをI2C_1に接続していることを設定
LPS25H.Init()
#LPS25H特有の初期化を行います。
while 1:
#無限ループ文 終了するときはキーボードでCtrl+Cを押します。
    print "P:%d" % LPS25H.Press()
    #気圧データを取得します。単位はhPa(ヘクトパスカル)
    print "T:%d" % LPS25H.Temp()
    #温度データを取得します。単位は℃
    time.sleep(0.1)
    #100ミリ秒待ちます
