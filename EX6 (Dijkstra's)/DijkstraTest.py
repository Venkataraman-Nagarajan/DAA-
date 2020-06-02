from ShortestPath import ShortestPath
from WeightedDigraph import WeightedDigraph

def main():
	# creating a graph
	edges = [(2, 1, 3), (1, 3, 6), (1, 4, 3), (4, 2, 1), (5, 2, 4), (5, 4, 2), (4, 3, 1), (3, 4, 2)]
	n_vertices = 5
	source = 1

	graph = WeightedDigraph(n_vertices)
	graph.EdgeWeightedDigraph(edges)
	
	sp = ShortestPath(graph, source)
	sp.dijkstraSP()
	print(sp)	

if __name__ == '__main__':
	main()

'''
Source: 1

Graph:
Number of vertices: 5
Number of edges: 8
Edge from 2 to 1 Weight: 3
Edge from 1 to 3 Weight: 6
Edge from 1 to 4 Weight: 3
Edge from 4 to 2 Weight: 1
Edge from 5 to 2 Weight: 4
Edge from 5 to 4 Weight: 2
Edge from 4 to 3 Weight: 1
Edge from 3 to 4 Weight: 2

To Vertex: 2 Distance: 4 Path: ['1', '4', '2']
To Vertex: 3 Distance: 4 Path: ['1', '4', '3']
To Vertex: 4 Distance: 3 Path: ['1', '4']
To Vertex: 5 Distance: inf Path: No Path
'''