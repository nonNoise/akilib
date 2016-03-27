# -*- encoding:utf8 -*-
from akilib import AKI_I2C_HDC1000
#akilibライブラリのAKI_I2C_HDC1000を使用することを宣言
import time
#timeライブラリ

x = AKI_I2C_HDC1000(1)
#HDC1000をI2C_1で使用する事を宣言
x.Config()
#HDC1000特有の初期化処理を行います。

while 1:
#無限ループ文 終了するときはキーボードでCtrl+Cを押します。
	print "%d 'C" % x.Temperature()
    #温度を取得します。表記は℃
	print u"%d /" % x.Humidity()
    #湿度を取得します。表記は％
	time.sleep(1)
    #1秒待ちます。




