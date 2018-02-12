#!/usr/bin/python
import sys
from PIL import Image, ImageTk, ImageDraw
import tkinter as tk 
from tkinter import ttk
from printer import *
from Blob import *
import time
import threading

t1 = 0
t2 = 0
def task(root):
    ft = ttk.Frame()
    ft.pack(expand=True, fill=tk.BOTH, side=tk.TOP)
    '''
    task.pb_hD = ttk.Progressbar(ft, orient='horizontal', mode='indeterminate')
    task.pb_hD.pack(expand=True, fill=tk.BOTH, side=tk.TOP)
    task.pb_hD.start(100)
    '''
    root.mainloop()

def bSearch(l, t):
	i = int(len(l)/2)
	if i < 1:
		return None
	if l[i].coord == t and l[i].label is None:
		return l[i]
	elif l[i].coord[1] < t[1]:
		return bSearch(l[i:], t)
	elif l[i].coord[1] > t[1]:
		return bSearch(l[:i], t)
	else:
		if l[i].coord[0] < t[0]:
			return bSearch(l[i:], t)
		elif l[i].coord[0] > t[0]:
			return bSearch(l[:i], t)

def updateImage():
	pic = ImageTk.PhotoImage(imgRGB)
	run.l["image"] = pic
	run.l.image = pic
	#run.top.after(1, colors)

def main(root):
	main.blobs = []
	pixs = []
	points = []
	lbl = 1
	img = imgRGB.convert("1")
	drw = ImageDraw.Draw(imgRGB)
	for y in range(img.size[1]):
		for x in range(img.size[0]):
			if img.getpixel((x, y)) == 0: 
				points.append(Point(x,y))
		
	for i in range(len(points)):
		p = points[i]
		if p.label is None:
			p.label = lbl
			pixs.insert(0, p)
			while len(pixs) > 0:
				pon = pixs.pop()
				temp = pon.coord
				temps = ((temp[0]+1, temp[1]), (temp[0], temp[1]+1), (temp[0], temp[1]-1), (temp[0]-1, temp[1])) 
								#right,									down,									up,								 left
				#temps = ((temp[0]+1, temp[1]), (temp[0], temp[1]+1), (temp[0]-1, temp[1]), (temp[0], temp[1]-1), (temp[0]-1, temp[1]-1), (temp[0]+1, temp[1]-1), (temp[0]-1, temp[1]+1), (temp[0]+1, temp[1]+1))
				for t in temps:
					if img.getpixel(t) == 0:
						inp = bSearch(points, t)
						if inp is not None:
							inp.label = pon.label
							pixs.insert(0, inp)
			lbl += 1
	for b in range(lbl-1):
		main.blobs.append(Blob())
	for p in points:
		main.blobs[p.label-1].add(*p.coord)

	t2 = time.clock() - t1
	print("Size:", imgRGB.size)
	print("Points:", len(points))
	print("Blobs:", len(main.blobs))
	print("Finished in: " + str(t2) + "s")

	for bl in main.blobs:
		drw.rectangle([tuple(bl._min), tuple(bl._max)] , outline=(255, 0, 0))
		bl.chunk = imgRGB.crop((bl._min[0], bl._min[1], bl._max[0], bl._max[1]))
	#imgRGB.putpixel((255, 0, 0))
	'''
	for p in main.blobs[4].points:
		imgRGB.putpixel(p, (0, 255, 0))
		updateImage()
	'''
	print('Done')
	updateImage()
	#task.pb_hD.destroy()
	
	pf = PathFinder(main.blobs[4])
	print(main.blobs[4].size[0] * main.blobs[4].size[1])
	print(len(pf.points))
	pf.fill()
	print(len(pf.points))
	
	for r in range(len(pf.points)):
		for c in range(len(pf.points[r])):
			if pf.points[r][c] != -1:
				imgRGB.putpixel(pf.points[r][c], (0, 0, 255))
			else:
				imgRGB.putpixel((pf.blob._min[0] + c, pf.blob._min[1] + r), (0, 255, 0))
	
	updateImage()

	'''
	for r in pf.points:
		for	c in r: 
			if c is not -1:
				print("|", end="")
			else:
				print("_", end="")
		print()
	'''
def run():
	run.top = tk.Tk()
	pic = ImageTk.PhotoImage(imgRGB)
	run.l = tk.Label(run.top, image=pic)
	run.l.image = pic
	run.l.pack()

	t1=threading.Thread(target=main, args=(run.top,))
	t2 = time.clock()
	t1.start()
	task(run.top) 
	t1.join()




if __name__ == "__main__":
	
	imgRGB = Image.open(sys.argv[-1])
	run()
