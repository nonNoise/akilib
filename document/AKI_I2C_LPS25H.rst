=================================================
AKI_I2C_LPS25H
=================================================



:Title: LPS25H 気圧センサー
:Device: Edison,RaspberryPi A+,B+,2B,3B
:URL: http://akizukidenshi.com/catalog/g/gK-08338/
:PDF: http://www.st-japan.co.jp/st-web-ui/static/active/jp/resource/technical/document/datasheet/DM00066332.pdf
:Version: ver1.0
:BusType: I2C接続

.. image:: img/LPS25H.png
    :width: 480px

How to use 使い方
-----------------------------------------------

::

    from akilib import AKI_I2C_LPS25H

    LPS25H = AKI_I2C_LPS25H(1)

    LPS25H.Init()

    LPS25H.Press()

    LPS25H.Temp()


:Project Title: AKI_I2C_LPS25H
:Development Date:  2016/03/12
:Development Leader: Yuta Kitagami.
:Related to library: mraa
:Version:  2016/03/12   ver1.0
