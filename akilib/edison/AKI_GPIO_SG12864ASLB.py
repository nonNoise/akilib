import mraa
import time
from struct import *



class AKI_GPIO_SG12864ASLB:
	def __init__(self,RS,RW,E,D0,D1,D2,D3,D4,D5,D6,D7,CS1,CS2,Reset):
		self.HI = 1
		self.LOW = 0	
		self.RS = mraa.Gpio(RS) 
		self.RW = mraa.Gpio(RW) 
		self.E = mraa.Gpio(E) 
		self.DB0 = mraa.Gpio(D0)
		self.DB1 = mraa.Gpio(D1)
		self.DB2 = mraa.Gpio(D2) 
		self.DB3 = mraa.Gpio(D3) 
		self.DB4 = mraa.Gpio(D4) 
		self.DB5 = mraa.Gpio(D5) 
		self.DB6 = mraa.Gpio(D6) 
		self.DB7 = mraa.Gpio(D7) 
		self.CS1 = mraa.Gpio(CS1) 
		self.CS2 = mraa.Gpio(CS2) 
		self.Reset = mraa.Gpio(Reset) 

		self.RS.useMmap(True) 
		self.RW.useMmap(True)
		self.E.useMmap(True)
		self.DB0.useMmap(True)
		self.DB1.useMmap(True)
		self.DB3.useMmap(True) 
		self.DB4.useMmap(True)
		self.DB5.useMmap(True) 
		self.DB6.useMmap(True)
		self.DB7.useMmap(True)
		self.CS1.useMmap(True) 
		self.CS2.useMmap(True)
		self.Reset.useMmap(True)
		

		self.RS.dir(mraa.DIR_OUT)
		self.RW.dir(mraa.DIR_OUT)
		self.E.dir(mraa.DIR_OUT)
		self.DB0.dir(mraa.DIR_OUT)
		self.DB1.dir(mraa.DIR_OUT)
		self.DB2.dir(mraa.DIR_OUT)
		self.DB3.dir(mraa.DIR_OUT)
		self.DB4.dir(mraa.DIR_OUT)
		self.DB5.dir(mraa.DIR_OUT)
		self.DB6.dir(mraa.DIR_OUT)
		self.DB7.dir(mraa.DIR_OUT)
		self.CS1.dir(mraa.DIR_OUT)
		self.CS2.dir(mraa.DIR_OUT)
		self.Reset.dir(mraa.DIR_OUT)
		
		self.RS.write(self.LOW)
		self.RW.write(self.LOW)
		self.E.write(self.LOW)
		self.DB0.write(self.LOW)
		self.DB1.write(self.LOW)
		self.DB2.write(self.LOW)
		self.DB3.write(self.LOW)
		self.DB4.write(self.LOW)
		self.DB5.write(self.LOW)
		self.DB6.write(self.LOW)
		self.DB7.write(self.LOW)
		self.CS1.write(self.LOW)
		self.CS2.write(self.LOW)
		self.Reset.write(self.LOW)
 		
 		#time.sleep(0.01)
		self.Reset.write(self.HI)
 		time.sleep(0.01)
		#time.sleep(0.01)	


		print "Init"
		try:
			from PIL import Image, ImageDraw
			self.SCREEN_WIDTH = 128
			self.SCREEN_HEIGHT = 64
			self.buffer = Image.new("1", (self.SCREEN_WIDTH,self.SCREEN_HEIGHT), "white") #
			self.draw = ImageDraw.Draw(self.buffer)
		except ImportError:
			raise NoSuchLibraryError('PIL')
	#===============================================================================#
	def Write_Command(self,data,cs):
		self.RS.write(self.LOW)
		self.DB0.write((data&0x01)>>0)
		self.DB1.write((data&0x02)>>1)
		self.DB2.write((data&0x04)>>2)
		self.DB3.write((data&0x08)>>3)
		self.DB4.write((data&0x10)>>4)
		self.DB5.write((data&0x20)>>5)
		self.DB6.write((data&0x40)>>6)
		self.DB7.write((data&0x80)>>7)
		if (cs == 0):
			self.CS1.write(self.HI)
			self.CS2.write(self.LOW)
		else :
			self.CS1.write(self.LOW)
			self.CS2.write(self.HI)
		self.E.write(self.LOW)
		self.E.write(self.HI)
		self.E.write(self.LOW)
		#time.sleep(0.0001)		
	#===============================================================================#
	def Write_Data(self,data,cs):
		self.RS.write(self.HI)
		self.E.write(self.LOW)
		self.DB0.write((data&0x01)>>0)
		self.DB1.write((data&0x02)>>1)
		self.DB2.write((data&0x04)>>2)
		self.DB3.write((data&0x08)>>3)
		self.DB4.write((data&0x10)>>4)
		self.DB5.write((data&0x20)>>5)
		self.DB6.write((data&0x40)>>6)
		self.DB7.write((data&0x80)>>7)
		if (cs == 0):
			self.CS1.write(self.HI)
			self.CS2.write(self.LOW)
		else :
			self.CS1.write(self.LOW)
			self.CS2.write(self.HI)
		self.E.write(self.LOW)
		self.E.write(self.HI)
		self.E.write(self.LOW)
		#time.sleep(0.0001)		
	#===============================================================================#
	def SetUp(self):
		self.Write_Command(0xC0,0) #Display StartLine 
		self.Write_Command(0x3F,0) #Display ON
		self.Write_Command(0xC0,1) #Display StartLine
		self.Write_Command(0x3F,1) #Display ON

	#===============================================================================#
	def SetPosData(self,x,y,deta):
		if( x < 64 ):
			self.Write_Command(0x40 | (x & 0x3F),0)
			self.Write_Command(0xB8 | (y & 0x07),0)
			self.Write_Data(deta,0)
		else	:
			self.Write_Command(0x40 | (x & 0x3F),1)
			self.Write_Command(0xB8 | (y & 0x07),1)
			self.Write_Data(deta,1)
	#===============================================================================#
	def Clear(self):
		for y in range(8):
			for x in range(128):
				self.SetPosData(x,y,0x00)
		del self.buffer
		del self.draw
		from PIL import Image, ImageDraw
		self.buffer = Image.new("1", (self.SCREEN_WIDTH,self.SCREEN_HEIGHT), "white") #"white"
		self.draw = ImageDraw.Draw(self.buffer)
	#===============================================================================#
	def Test(self):
		for y in range(8):
			for x in range(128):
				self.SetPosData(x,y,0x0F)
	#===============================================================================#
	def Pixel_Check(self,x,y):
		if(self.buffer.getpixel((x,y)) > 127):
			return 1
		else :
			return 0
	#===============================================================================#
	def Uplode(self):
		for y in range(8):
			for x in range(128):
				#print i,j,((0+(8*i))<<0)
				data = 0
				data = data | self.Pixel_Check(x,(0+(8*y)))<<0
				data = data | self.Pixel_Check(x,(1+(8*y)))<<1
				data = data | self.Pixel_Check(x,(2+(8*y)))<<2
				data = data | self.Pixel_Check(x,(3+(8*y)))<<3
				data = data | self.Pixel_Check(x,(4+(8*y)))<<4
				data = data | self.Pixel_Check(x,(5+(8*y)))<<5
				data = data | self.Pixel_Check(x,(6+(8*y)))<<6
				data = data | self.Pixel_Check(x,(7+(8*y)))<<7
				self.SetPosData(x,y,~data)
				#print data ,
			#print ""
		#self.buffer.save("img.png", "PNG")	
		del self.buffer
		del self.draw
		from PIL import Image, ImageDraw
		self.buffer = Image.new("1", (self.SCREEN_WIDTH,self.SCREEN_HEIGHT), "white") #"white"
		self.draw = ImageDraw.Draw(self.buffer)
		
	#===============================================================================#
	def Save(self,filename):
		self.buffer.save(filename, "PNG")	

