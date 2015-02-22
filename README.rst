=========================================================
akilib project
=========================================================

2015.02.23 まだ準備中です。


0.初めに
-----------------------------------------

akilibプロジェクトは、秋葉原で購入出来る部品をライブラリ化し、次世代であるシングルコンピュータで手軽に取り扱えるようにするプロジェクトである。

現在は、Pythonが主であり、サブでC言語を取り入れているが、皆様のご支援によりRubyやGoに移植されることを願っています。

1.ライブラリ情報
-----------------------------------------

- Raspberry Pi
    - AKI_I2C_AQM1602A
        - Ｉ２Ｃ接続小型キャラクタＬＣＤモジュール
        - http://akizukidenshi.com/catalog/g/gK-08896/   
        - ver 0.3 β
        - I2C接続
    - AKI_I2C_HDC1000
        - 温湿度センサーモジュール
        - http://akizukidenshi.com/catalog/g/gM-08775/
        - ver1.0
        - I2C接続
    - AKI_I2C_LPS25H
        - 圧力センサーモジュール
        - http://akizukidenshi.com/catalog/g/gK-08338/
        - ver1.0
        - I2C接続
    - AKI_I2C_MCP3425
        - １６Ｂｉｔ　ＡＤ変換モジュール
        -  http://akizukidenshi.com/catalog/g/gK-08018/
        - ver 1.0
        - I2C接続



- Edison
    - AKI_AQM1248A
        - 超小型グラフィックＬＣＤ
        - http://akizukidenshi.com/catalog/g/gK-07007/
        - ver0.8 α
        - SPI接続
    - AKI_I2C_AQM0802A
        - 小型キャラクタＬＣＤモジュール　８ｘ２行
        - http://akizukidenshi.com/catalog/g/gP-06669/
        - ver 1.0
        - I2C接続
    - AKI_I2C_HDC1000
        - 温湿度センサーモジュール
        - http://akizukidenshi.com/catalog/g/gM-08775/
        - ver1.0
        - I2C接続
    - AKI_I2C_SO1602AWYB
        - 有機ＥＬキャラクタディスプレイモジュール　１６ｘ２行
        - http://akizukidenshi.com/catalog/g/gP-08278/
        - ver 1.0
        - I2C接続
    - AKI_SG12864ASLB
        - グラフィック液晶表示器　１２８ｘ６４ドット
        - http://akizukidenshi.com/catalog/g/gP-02159/
        - ver 1.0
        - GPIO接続


※バージョン表記に関して
ver 1.0以下の物は、ひとまず動くけど、たまに動かない。所謂、難有り状態です。


2.ToDo
-----------------------------------------

とりあえず公開版です。

ソースの整備もできてません。

回路図もライブラリに含めたいです。

うまく行けばmraaでRasPiもEdisonも同じライブラリで行けるかも。

ライブラリが某店に偏るのも如何なものかと悩み中。他店展開も考え中。

作ってほしいライブラリが有りましたら :Twitter:@nonNoise まで。


3.ライセンスに関して
-----------------------------------------

『自由で無保証で勝手に使っていいよ、ただし作者明記はちゃんとしてね』  的なライセンスであるMITライセンスを採用しました。

ソースには以下のような作者及び協力者の名前を付けたいと思います。

商用に使用する際も、以下の表記は削除しないでください。


    The MIT License (MIT)
    
    Copyright (c) 2015 Yuta KItagami
