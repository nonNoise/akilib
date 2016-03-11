# -*- encoding:utf8 -*-
import mraa
from akilib import AKI_GPIO_SG12864ASLB
import time
import datetime
from PIL import Image, ImageDraw,ImageFont
g = AKI_GPIO_SG12864ASLB(13,12,11,10,9,8,7,6,5,4,3,2,1,0)

g.SetUp()
g.Clear()
g.Test()
#g.Close()



#g.Write_Command(0x80,0)
#g.E.write(g.HI)
#g.Crear()

#g.draw.ellipse((2, 2, 42, 42),outline="#ffffff")
#g.draw.ellipse((32, 32, 52, 52),outline="#ffffff")
#g.draw.rectangle(((10,0),(20,5)),fill="#ffffff")

#pic = Image.open('01.png')
#g.buffer.paste(pic,(0, 0))
font = ImageFont.truetype('ipag.ttf', 12)
g.draw.text((1, 10), u'こんにちは、Edison。', font=font, fill='#000')
g.draw.text((1, 25), u'新しい世界へようこそ', font=font, fill='#000')
g.Uplode()

g.Clear()
while 1:
    d = datetime.datetime.today()
    font = ImageFont.truetype('ipag.ttf', 22)
    g.draw.text((1, 5),u'%s月%s日' % (d.month, d.day) , font=font, fill='#000')
    g.draw.text((1, 25),u'%s時%s分%s秒' % (d.hour, d.minute, d.second,), font=font, fill='#000')
    g.Uplode()

print "End."
