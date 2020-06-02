from Heap import Heap

class VertexData(object):
	def __init__(self, vertex, dist, path):
		self.vertex = vertex
		self.dist = dist
		self.path = path

	# for comparison and index
	def __lt__(self, v_pair):
		return self.dist < v_pair.dist

	# for heap print:
	def __str__(self):
		return 'V:{} D:{} P:{}'.format(self.vertex, self.dist, self.path)


class ShortestPath(object):
	# source vertex and graph (WeightedDigraph object) to analyse.
	def __init__(self, graph, source):
		self.graph = graph
		self.source = source

		# heap initialisation
		self.dist_heap = Heap(graph.V_(), keyfunc=lambda x: x.vertex, initval=VertexData(-1, -10**9, ''))
		
		# create dist map:
		self.dists = {}
		self.dist_map()

		# creating the heap
		self.dist_heap.create_heap([VertexData(vert, *self.dists[vert]) for vert in self.dists])

 	# path and distance functions
	def dist_to(self, vertex):
		if vertex not in self.dists:
			raise Exception('Invalid Vertex!')		
		return self.dists[vertex][0]

	# check path existence
	def has_path_to(self, vertex):
		if vertex not in self.dists:
			raise Exception('Invalid Vertex!')
		return self.dists[vertex][0] != 10 ** 9

	# get method
	def path_to(self, vertex):		
		return self.dists[vertex][1]

	# to create dist_map
	def dist_map(self):
		# adjacency list for source -> vertices list
		adj_list = list(zip(*self.graph.adj(self.source)))[0]
		for vert in self.graph:
			if vert != self.source:
				if vert not in adj_list:
					self.dists[vert] = 10 ** 9, '' # infinity
				else:
					self.dists[vert] = self.graph.vertices[self.source][adj_list.index(vert)][1], ''		

	# to relax a vertex
	def relax(self, vert):
		for adj_edge in self.graph.adj(vert):
			# if a shorter path exists
			if adj_edge[0] != self.source and self.dists[vert][0] + adj_edge[1] < self.dists[adj_edge[0]][0]:
				self.dists[adj_edge[0]] = [self.dists[vert][0] + adj_edge[1], str(vert)]
				# heap update
				self.dist_heap.decrease_key(adj_edge[0], VertexData(adj_edge[0], *self.dists[adj_edge[0]]))

	# Implementing dijsktra's SSSP:
	def dijkstraSP(self):
		for _ in range(self.graph.V_() - 1):
			vert = self.dist_heap.delete_min()
			self.relax(vert.vertex)

	# to print the shortest paths:
	def __str__(self):
		st = 'Source: {}\n\n'.format(self.source)
		st += 'Graph: \n' + str(self.graph) + '\n\n'
		for vert in self.dists:
			temp = [str(vert)]
			if not self.has_path_to(vert):
				temp = 'No Path'
			else:
				path = self.dists[vert][1]
				while path != '':
					temp.append(path)
					path = self.dists[int(path)][1]
				temp.append(str(self.source))
				temp = temp[::-1]
			st += 'To Vertex: {} Distance: {} Path: {}'.format(vert, 'inf' if self.dists[vert][0]==10**9 else self.dists[vert][0], temp) + '\n'
		return st
