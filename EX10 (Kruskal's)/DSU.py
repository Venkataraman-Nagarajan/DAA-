def FIND(e,parent):
		if(parent[e]==e):
			return e
		return FIND(parent[e],parent)

def UNION(src,dest,parent):
	x = FIND(src,parent)
	y = FIND(dest,parent)
	parent[x] = y
	return parent
	
def initialize_graph(V,E):
	parent = [_ for _ in range(V+1)]
	visited = [0 for _ in range(E)]	
	Edge = []
	print("\nEnter ",E," edges(source, destn, weight) : ")
	for _ in range(E):
		print("\t",end="")
		src,dest,weight = [int(x) for x in input().split()]
		Edge.append((weight,src,dest))
	
	Edge.sort()
	return Edge,parent,visited
	
def find_spanning_tree(Edge,parent,visited,req_edges):

	for i in range(len(Edge)):
		weight,src,dest = Edge[i]
		if(req_edges==0):
			break
		if(FIND(src,parent) != FIND(dest,parent)):
			visited[i]=1
			parent = UNION(src,dest,parent)
			req_edges-=1
		
	return Edge,visited
		
def print_spanning_tree(Edge,visited,req_edges):
	Sum = 0
	for i in range(len(Edge)):
		weight,src,dest = Edge[i]
		if(visited[i]==1):
			Sum+=weight
	
	print("\nTotal Weight of spanning tree : ",Sum)
	print("\nEdges Added are :\n")
	
	for i in range(len(Edge)):
		weight,src,dest = Edge[i]
		if(visited[i]==1):
			print("\t",src," ",dest)
	
	print("-----------")

print("-- mst --")
print("\tNo. of Vertices : ",end="")
V = int(input())
print("\tNo. of Edges    : ",end="")
E = int(input())

Edge,parent,visited = initialize_graph(V,E)
Edge,visited = find_spanning_tree(Edge,parent,visited,V-1)
print_spanning_tree(Edge,visited,V-1)

'''
venky@venky-Inspiron-5570:~/Downloads$ python3 DSU.py
-- mst --
	No. of Vertices : 4
	No. of Edges    : 4

Enter  4  edges(source, destn, weight) : 
	1 2 4
	2 3 5
	2 4 3
	1 4 2			

Total Weight of spanning tree :  10

Edges Added are :

	 1   4
	 2   4
	 2   3
-----------

venky@venky-Inspiron-5570:~/Downloads$ python3 DSU.py
-- mst --
	No. of Vertices : 7
	No. of Edges    : 11

Enter  11  edges(source, destn, weight) : 
	1 2 7
	2 3 8
	1 4 5
	3 5 5
	4 2 9
	2 5 7
	4 5 15
	4 6 6
	6 5 8
	6 7 11
	5 7 9
										
Total Weight of spanning tree :  39

Edges Added are :

	 1   4
	 3   5
	 4   6
	 1   2
	 2   5
	 5   7
-----------

'''
