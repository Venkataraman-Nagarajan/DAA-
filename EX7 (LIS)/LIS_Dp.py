print("Enter the array : ",end="")
arr = [int(_) for _ in input().split() ]
arr.append(0x7f7f7f7f7f7f7f)
ans=[]
l = [ 1 for i in range(len(arr))]
p = [-1 for i in range(len(arr))]

def TraceLIS_rec(n):
	if(n==-1):
		return;
	if(p[n]!=-1):
		ans.append(arr[p[n]])
	TraceLIS_rec(p[n])
	
	
def TraceLIS_itr():
	i=len(p)-1
	while(p[i]!=-1):
		ans.append(arr[p[i]])
		i=p[i]


for i in range (1,len(arr)):
	for j in range(0,i):
		if(arr[i]>arr[j]):
			#l[i] = max(l[i],l[j]+1)
			if(l[i]<l[j]+1):
				l[i]=l[j]+1
				p[i]=j


print("LIS Count is    : ",end="")
print(l[len(l)-1]-1)
print("LIS Array is    : ",end="")
#print(l);

#TraceLIS_itr()
TraceLIS_rec(len(p)-1)
print(ans[::-1])

"""
cs1192@splc30:~/DAA LAB/LIS$ python3 LIS_Dp.py 
Enter the array : 5 2 8 6 3 6 9 7
LIS Count is    : 4
LIS Array is    : [2, 3, 6, 9]

cs1192@splc30:~/DAA LAB/LIS$ python3 LIS_Dp.py 
Enter the array : 2 4 3 5 1 7 6 9 8
LIS Count is    : 5
LIS Array is    : [2, 4, 5, 7, 9]

cs1192@splc30:~/DAA LAB/LIS$ python3 LIS_Dp.py 
Enter the array : 5 1 5 7 2 4 9 8
LIS Count is    : 4
LIS Array is    : [1, 5, 7, 9]

cs1192@splc30:~/DAA LAB/LIS$ python3 LIS_Dp.py 
Enter the array : 3 1 4 1 5 9 2 6 5 3 5 8 9 7 9 3 2 3 8 4 6 2 6
LIS Count is    : 6
LIS Array is    : [3, 4, 5, 6, 8, 9]

"""
