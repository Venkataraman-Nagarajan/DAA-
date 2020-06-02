class DirectedEdge(object):

	# constructor to create the edge
	def __init__(self, fr, to, w):
		self.fr_v = fr
		self.to_v = to
		self.w = w

	# print format
	def __str__(self):
		return 'Edge from {} to {} Weight: {}'.format(self.fr_v, self.to_v, self.w)

	# get methods:

	def weight(self):
		return self.w
	
	def from_(self):
		return self.fr_v

	def to(self):
		return self.to_v