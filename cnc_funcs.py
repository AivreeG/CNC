import serial
import sys
from PIL import Image, ImageTk
import tkinter as tk 
from printer import *

#ser = serial.Serial("COM9", 9600, timeout=0)

def findNth(str, c, n):
	try:
		i = 0
		for s in range(len(str)):
			if str[s] == c:
				i += 1
			if i == n:
				return s
	except e:
		print(e)
	finally:
		return s

def readBMP(img, width, height):
	nls = []
	pnts = []
	wtsp = []

	for r in range(height):
		pnts.append([])
		wtsp.append([])
		for c in range(1, width * 3 -1):
			if img[c-1] == img[c] and img[c+1] == img[c]:
				if img[c] == '\xff':
					wtsp[r].append("{} {}".format(r, c))
				elif img[c] == '\x00':
					pnts[r].append("{} {}".format(r, c))
			elif img[c-1] != img[c] and img[c+1] != img[c]:
				nls.append(c)
	return (pnts, wtsp, nls)  

def asciiBMP(img, pwidth):
		str = ""
		img = img.convert("1")
		for l in range(img.size[1]):
				for p in range(img.size[0]):
						if not img.getpixel((p, l)): 
								str =  str + " "*pwidth
						else: str = str + u"\u2588"*pwidth
				str += "\n"
		return str
						
def colors():
	for bl in main.blobs:
		for p in bl.points:
			imgRGB.putpixel(p, (colors.r, colors.g, colors.b))
	if colors.r < 256 and colors.g == 0:
		colors.r += 1
	else:
		if colors.g < 256 and colors.b == 0:
			colors.g += 1
			colors.r -= 1
		else:
			if colors.b < 256 and colors.r == 0:
				colors.b += 1
				colors.g -= 1
			else:
				colors.b -= 1
	updateImage()
colors.r = 0
colors.g = 0
colors.b = 0
'''
f = a[-4:53:-1]
ls = findNL(f, "\x00")
e = list(f)
for i in ls[::-1]:
  e.pop(i)

outp = open("outs.txt", "w")
outp.write(printBMP(list(b)))
outp.close()
st = "0123456789"
#print(st[::3])
'''
'''
class BitMap:
	def __init__(self, path, size, new_line='\x00'):
		self._path = path
		self._size = size
		self._nl = new_line
		self._data = open(self._path, "r").read()
		
	def findNL(self, char):
		nls = []
		for c in range(1, len(char)):
			if self._data[c] == char:
				if self._data[c-1] != char and self._data[c+1] != char:
					nls.append(c)
		return nls
	
	def readData(self):
		pnts = []
		pxs = self._data[::3]
		i = 0
		for r in range(1, self._height):
			for c in range(1, self._width):
				if pxs[i] == "\x00":
					pnts.append("{} {}".format(r, c)) 
					i += 1    
		return pnts
		
	def printBMP(self):
		#ls = self.findNL(self._nl)
		img = self.data[:]
		#for i in ls[::-1]:
		#	img[i] 
		img.replace('\xff{}\xff'.format(self._nl), '\xff\n\xff') 
		img = "".join(img)
		img = img.replace("\x00", "|")
		img = img.replace("\xff", "_")
		return img
		class Printer:
	def __init__(self, points, img, serial):
		self.points = points
		self.img = img
		self.data = (self.img).data
		self.ser = serial
	def sendCoords(data):
		data = bytes(data, "UTF-8")
		ser.write(data)

	@property
	def path(self):
		return self._path
	@property
	def size(self):
		return self._size
	@property
	def new_line(self):
		return self._nl
	@property
	def data(self):
		return self._data
	def dimensions(self):
		return (self._width, self._height)
'''

img = Image.open("10x13-outputW.bmp")
if __name__ == "__main__":
    
    print(asciiBMP(img))

    '''
    img = img.convert("L")
    pixs = []
    for k in range(img.size[1]):
        for i in range(img.size[0]):
            if img.getpixel((i, k)) < 127: 
                #pixs.append((i, k)) 
                img.putpixel((i, k), 127)

    #print(pixs)
    top = tk.Tk()
    pic = ImageTk.PhotoImage(img)
    lbl = tk.Label(top, image=pic)
    lbl.image = pic
    lbl.pack()
    top.mainloop()
    '''
