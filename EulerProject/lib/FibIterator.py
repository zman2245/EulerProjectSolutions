class FibonacciIterator:

	def __init__(self):
		self.i 			= 1
		self.j 			= 1
		self.termNum	= 2

	def getCurrentVal(self):
		return self.j

	def getCurrentTermNum(self):
		return self.termNum

	def inc(self):
		tmp 			= self.i
		self.i 			= self.j
		self.j 			= tmp + self.j
		self.termNum 	+= 1
