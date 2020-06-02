print("Enter no of queens  : ",end=" ")
n = int(input())

queen = 1
free = 0

def print_board(visited):
	for i in visited:
		for j in i:
			if(j):
				print("Q",end=" ")
			else:
				print("-",end=" ")
		print()
	print()

def is_safe_state(r,c,visited):
	for k in range(n):
		if(visited[k][c]==queen):
			return False
		if(visited[r][k]==queen):
			return False

	k = r-1
	t = c-1
	while(k>=0 and t>=0):
		if(visited[k][t]==queen):
			return False
		k-=1
		t-=1

	k = r-1
	t = c+1
	while(k>=0 and t<n):
		if(visited[k][t]==queen):
			return False
		k-=1
		t+=1

	return True

def solve(i,visited):
	if(i==n):
		print("Solution exists")
		print_board(visited)
		return True
	for j in range(n):
		if(is_safe_state(i,j,visited)):
			visited[i][j] = queen
			if(solve(i+1,visited)):
				return True
			visited[i][j] = free
	return False

visited = [[free for i in range(n)]for j in range(n)]
if(solve(0,visited)==False):
	print("No Solution exists\n")

'''
venky@venky-Inspiron-5570:~/DAA/nQueensProb$ python3 nqueen.py 
Enter no of queens  :  4
Solution exists
- Q - - 
- - - Q 
Q - - - 
- - Q - 

venky@venky-Inspiron-5570:~/DAA/nQueensProb$ python3 nqueen.py 
Enter no of queens  :  3
No Solution exists

venky@venky-Inspiron-5570:~/DAA/nQueensProb$ python3 nqueen.py 
Enter no of queens  :  8
Solution exists
Q - - - - - - - 
- - - - Q - - - 
- - - - - - - Q 
- - - - - Q - - 
- - Q - - - - - 
- - - - - - Q - 
- Q - - - - - - 
- - - Q - - - - 

venky@venky-Inspiron-5570:~/DAA/nQueensProb$ python3 nqueen.py 
Enter no of queens  :  5
Solution exists
Q - - - - 
- - Q - - 
- - - - Q 
- Q - - - 
- - - Q - 


'''