def Input(m,n):
    print("Enter ",end="")
    print(m,end="")
    print("*",end="")
    print(n,end="")
    print(" matrix - : ")
    mat1 = [[int(input()) for j in range(m)] for i in range(n)]
    return mat1

def Print(mat):
    for i in mat:
        print()
        for j in i:
        	print(j,end="\t")
	#print()

def Multiply(mat1,mat2):
    result = [[0 for j in range(len(mat2[0]))] for i in range(len(mat1))]
    for i in range(len(mat1)):
	    for j in range(len(mat2[0])):
		    for k in range(len(mat2)):
			    result[i][j] += mat1[i][k] * mat2[k][j]
    return result

def fast_pow(x,n):
	if(n==1):
		return x
	elif(n%2 !=0):
		 return Multiply(x, fast_pow(x,n-1))
	else:
		return Multiply(fast_pow(x,n//2), fast_pow(x,n//2))


def fibonacciFinder(n):
    basematrix = [[0,1],[1,1]]
    basevalues = [[0],[1]]
    basematrix = fast_pow(basematrix,n)
    fibomatrix = Multiply(basematrix,basevalues)

    print("The ",n,"th Fibonacci Number is: ",fibomatrix[0][0])




print("Matrix Multiplication (A * B)--\n")
m,p,n = map(int, input("Enter as Rows(A),Cols(A),Cols(B) : ").split())
mat1= Input(m,p)
mat2= Input(p,n)
print("\n\nMatrix A: \n")
Print(mat1)
print("\n\nMatrix B: \n")
Print(mat2)
print("\n\nResult Matrix: \n")
result = Multiply(mat1,mat2)
Print(result)

exp = int(input("\n\nEnter power A is to be raised : "))
expomat = fast_pow(mat1,exp)
Print(expomat)

n = int(input("\n\nEnter n to get nth Fibonacci number : "))
fibonacciFinder(n)



"""
venky@venky-Inspiron-5570:~/DAA/EX2$ python3 Matrices.py 
Matrix Multiplication (A * B)--

Enter as Rows(A),Cols(A),Cols(B) : 2 2 2
Enter 2*2 matrix - : 
1
1
1
1
Enter 2*2 matrix - : 
2
2
2
2


Matrix A: 


1	1	
1	1	

Matrix B: 


2	2	
2	2	

Result Matrix: 


4	4	
4	4	

Enter power A is to be raised : 3

4	4	
4	4	

Enter n to get nth Fibonacci number : 4
The  4 th Fibonacci Number is:  3

"""
