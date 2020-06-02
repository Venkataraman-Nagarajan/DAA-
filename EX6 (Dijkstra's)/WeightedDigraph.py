from DirectedEdge import DirectedEdge

class WeightedDigraph(object):
	# graph initialisation.
	def __init__(self, n_vertex):
		self.V = n_vertex
		self.E = 0
		self.edges_ = []    # edge list
		self.vertices = {} # adjacency + distance list 
		for vert in range(1, self.V + 1):
			self.vertices[vert] = []

	# list of edges
	def EdgeWeightedDigraph(self, data):
		for fr, to, w in data:
			self.add_edge(DirectedEdge(fr, to, w))

	# printing the graph
	def __str__(self):
		st = 'Number of vertices: {}\nNumber of edges: {}'.format(self.V, self.E)
		for edge in self.edges_:
			st += '\n' + str(edge)
		return st

	# for iterating through the vertices
	def __iter__(self):
		self.vs = 0
		return self

	def __next__(self):
		if self.vs == self.V:
			raise StopIteration
		self.vs += 1
		return self.vs

	def V_(self):
		return self.V

	def E_(self):
		return self.E

	def edges(self):
		return self.edges_

	def add_edge(self, e):
		self.edges_.append(e)
		self.vertices[e.from_()].append([e.to(), e.weight()])
		self.E+=1
	
	# returning list of adjacent vertices
	def adj(self, v):
		return self.vertices[v]