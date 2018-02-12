class Printer:
	def __init__(self, points, img, serial):
		self.points = points
		self.img = img
		self.ser = serial
	def sendCoords(data):
		data = bytes(data, "UTF-8")
		ser.write(data)
