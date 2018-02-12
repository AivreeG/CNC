
def distSq(x1, y1, x2, y2):
	return (x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1)

class PathFinder:
	def __init__(self, blob):
		self.blob = blob
		self.width = blob.size[0]
		self.height = blob.size[1]
		self.points = blob.points
		self.path = []

	def fill(self):
		xmin = self.blob._min[0]
		xmax = self.blob._max[0]
		ymin = self.blob._min[1]
		ymax = self.blob._max[1]
		i = 0
		while i < len(self.points) - 1:
			#print(self.points[i])
			if self.points[i][0] + 1 != self.points[i+1][0] and self.points[i][1] == self.points[i+1][1]:
				for p in range(self.points[i+1][0] - self.points[i][0]):
					self.points.insert(i+1, -1)
					i+=1
			i+=1
		temp = []
		for r in range(self.height):
			temp.append([])
			for c in range(self.width):
				if len(self.points) != 0:
					temp[r].append(self.points.pop(0))
		self.points = temp

	def spiral(self, cw=True):
		NORTH = 0
		EAST = 1
		SOUTH = 2
		WEST = 3
		columns = self.blob.size[0]
		rows = self.blob.size[1]
		r = 0
		c = 0
		switch = {NORTH : north,
							 EAST : east,
							SOUTH : south,
						 	 WEST : west}
		s = self.points[0]
		p = s
		self.path.append(s)
		if cw:
			facing = EAST
			while True:
				swtich[facing]()
				
				if p == s: break
		else:
			facing = SOUTH
	'''
	def north(self, p):
		p1 = (p[0]-1, p[1]-1)
		p2 = (p[0], p[1]-1)
		p3 = (p[0]+1, p[1]-1)
	def east(self, p):
		p1 = x+1 y-1
		p2 = x+1, y
		p3 = x+1, y+1
	def south(self, p):
		p1 = x+1, y+1
		p2 = x, y+1
		p3 = x-1, y+1
	def west(self, p):
		p1 = x-1, y+1
		p2 = x-1, y
		p3 = x-1, y-1
	'''
class Point:
	def __init__(self, x, y, lbl=None):
		self.coord = (x, y)
		self.label = lbl
'''
	def __lt__(self, p):
		return ((self.coord[0] < p.coord[0] and self.coord[1] == p.coord[1])) or ((self.coord[1] < p.coord[1] and self.coord[0] == p.coord[0]))
	def __gt__(self, p):
		return (self.coord[0] > p.coord[0] and self.coord[1] == p.coord[1]) or (self.coord[1] > p.coord[1] and self.coord[0] == p.coord[0])
	def __le__(self, p):
		return self.coord <= p.coord
	def __ge__(self, p):
		return self.coord >= p.coord
	def __eq__(self, p):
		return self.coord == p.coord
	def __ne__(self, p):
		return self.coord != p.coord
'''

class Blob:
	
	def __init__(self, x=None, y=None):
		if x is not None and y is not None:
			self._min = [x, y]
			self._max = [x, y]
			self.center = [(self._min[0] + self._max[0]) / 2, (self._min[1] + self._max[1]) / 2]
			self.points = [(x, y)]
			self.size = [self._max[0] - self._min[0], self._max[1] - self._min[1]]
			self.chunk = None
		else:
			self._min = []
			self._max = []
			self.center = []
			self.points = []
			self.size = [0, 0]
				
	def isNear(self, x, y, thresh):
		if (self._min[0] <= x and self._max[0] >= x) and (self._min[1] <= y and self._max[1] >= y):
			return True
		cx = max(min(x, self._max[0]), self._min[0])
		cy = max(min(y, self._max[1]), self._min[1])
		d = distSq(cx, cy, x, y)
		return d < thresh*thresh
	
	def add(self, x, y):
		if len(self._min) < 1 and len(self._max) < 1:
			self._min = [x, y]
			self._max = [x, y]
		else:
			self._min[0] = min(self._min[0], x)
			self._min[1] = min(self._min[1], y)
			self._max[0] = max(self._max[0], x)
			self._max[1] = max(self._max[1], y)
		self.center = [(self._min[0] + self._max[0]) / 2, (self._min[1] + self._max[1]) / 2]
		self.size = [self._max[0] - self._min[0], self._max[1] - self._min[1]]
		self.points.append((x, y))
