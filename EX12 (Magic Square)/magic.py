def odd_matrix(n):
	mat = [[0 for j in range(n)]for i in range(n)]
	'''
	start from (0,n/2) n move diagonally up and circularly if limits crossed
	'''
	num = 1
	i,j = 0,n//2
	while(num<=n*n):
		if(i<0 and j==n):
			i,j = 1,n-1
		else:
			if(i<0):
				i=n-1
			if(j==n):
				j=0

		if(mat[i][j]==0):
			mat[i][j] = num
			num+=1
		else:
			j-=1
			i+=2
			continue
		i-=1
		j+=1

	return mat

def doubly_even_matrix(n):
	'''
	x - - x
	- x x -
	- x x -
	x - - x

	x parts where where u subtract by n^2+1 , - places u ignore
	'''
	mat = [[(i)*n + (j+1) for j in range(n)] for i in range(n)]

	for i in range(0,n//4):
		for j in range(0,n//4):
			mat[i][j] = n*n+1-mat[i][j]

	for i in range(3*n//4,n):
		for j in range(0,n//4):
			mat[i][j] = n*n+1-mat[i][j]

	for i in range(3*n//4,n):
		for j in range(3*n//4,n):
			mat[i][j] = n*n+1-mat[i][j]

	for i in range(n//4):
		for j in range(3*n//4,n):
			mat[i][j] = n*n+1-mat[i][j]

	for i in range(n//4,3*n//4):
		for j in range(n//4,3*n//4):
			mat[i][j] = n*n+1-mat[i][j]

	return mat

def singly_even_matrix(n):
	mat = [[0 for j in range(n)]for i in range(n)]
	A = odd_matrix(n//2);
	B = change_mat(A,n//2 * n//2)
	C = change_mat(B,n//2 * n//2)
	D = change_mat(C,n//2 * n//2)

	'''
	Matrix of the form n = 2(2m+1) here n & m used have the same meaning
	A C
	D B
	matrix... swap bw A n d for m times excet middle
	Swap bw B n C for m-1 coloumns
	'''
	m = (n//2-1)//2
	for i in range(n//2):
		for j in range(m):
			if(i==m):
				A[i][j+1],D[i][j+1] = D[i][j+1],A[i][j+1]
			else:
				A[i][j],D[i][j] = D[i][j],A[i][j]
	
	for i in range(n//2):
		for j in range(n//2-m+1,n//2):
			B[i][j],C[i][j] = C[i][j],B[i][j]
			
	for i in range(n//2):
		for j in range(n//2):
			mat[i][j] 			= A[i][j]
			mat[n//2+i][j] 		= D[i][j]
			mat[i][n//2+j] 		= C[i][j]
			mat[n//2+i][n//2+j] = B[i][j]
	return mat

def change_mat(A,n):
	B = [[0 for i in range(len(A))]for j in range(len(A))]
	for i in range(len(A)):
		for j in range(len(A)):
			B[i][j] = A[i][j] + n
	return B

def print_matrix(mat):
	print()
	for i in mat:
		for j in i:
			print("%-4d "%j,end="")
		print()
	print()


print("--- Magic Square ---\n")
print("Enter n : ",end="")
n = int(input())

if(n!=2 and n>=0):
	if(n%2):
		mat = odd_matrix(n)
	elif(n%4==0):
		mat = doubly_even_matrix(n)
	else:
		mat = singly_even_matrix(n)
	print_matrix(mat)
else:
	print("\nMagic square cannot be created\n")

'''
venky@venky-Inspiron-5570:~/DAA/magicSquare$ python3 magic.py 
--- Magic Square ---

Enter n : 3

8    1    6    
3    5    7    
4    9    2    

venky@venky-Inspiron-5570:~/DAA/magicSquare$ python3 magic.py 
--- Magic Square ---

Enter n : 2

Magic square cannot be created

venky@venky-Inspiron-5570:~/DAA/magicSquare$ python3 magic.py 
--- Magic Square ---

Enter n : 4

16   2    3    13   
5    11   10   8    
9    7    6    12   
4    14   15   1    

venky@venky-Inspiron-5570:~/DAA/magicSquare$ python3 magic.py 
--- Magic Square ---

Enter n : 6

35   1    6    26   19   24   
3    32   7    21   23   25   
31   9    2    22   27   20   
8    28   33   17   10   15   
30   5    34   12   14   16   
4    36   29   13   18   11   

venky@venky-Inspiron-5570:~/DAA/magicSquare$ python3 magic.py 
--- Magic Square ---

Enter n : 9

47   58   69   80   1    12   23   34   45   
57   68   79   9    11   22   33   44   46   
67   78   8    10   21   32   43   54   56   
77   7    18   20   31   42   53   55   66   
6    17   19   30   41   52   63   65   76   
16   27   29   40   51   62   64   75   5    
26   28   39   50   61   72   74   4    15   
36   38   49   60   71   73   3    14   25   
37   48   59   70   81   2    13   24   35 
'''

