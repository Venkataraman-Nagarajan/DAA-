print("Enter the array : ",end="")
arr = [int(_) for _ in input().split() ]
arr.append(0x7f7f7f7f7f7f7f)

def L(j):
	best=1;
	for i in range(0,j):
		if(arr[i]<arr[j]):
			best = max(best,L(i)+1);
	return best

print("LIS Count is    : ",end="")
print(L(len(arr)-1)-1)

"""
cs1192@splc30:~/DAA LAB/LIS$ python3 LIS_Ex.py 
Enter the array : 5 2 8 6 3 6 9 7
LIS Count is    : 4

cs1192@splc30:~/DAA LAB/LIS$ python3 LIS_Ex.py 
Enter the array : 2 4 3 5 1 7 6 9 8
LIS Count is    : 5

cs1192@splc30:~/DAA LAB/LIS$ python3 LIS_Ex.py 
Enter the array : 5 1 5 7 2 4 9  8
LIS Count is    : 4

cs1192@splc30:~/DAA LAB/LIS$ python3 LIS_Ex.py 
Enter the array : 3 1 4 1 5 9 2 6 5 3 5 8 9 7 9 3 2 3 8 4 6 2 6
LIS Count is    : 6

"""
