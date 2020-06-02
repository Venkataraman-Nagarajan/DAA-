print("Maximal - Sum sub-array - Effiecient Algorithm ")
print("\nEnter the array : ",end="")
a=[int(_) for _ in input().split()]

n=len(a)
maxi = -1
maxj = -1
maxsum=0;
cursum=0

for i in range(n):
	cursum+=a[i]
	if(cursum<0):
		cursum=0
		maxi=i+1
		maxj=i+2
	if(cursum > maxsum):
		maxsum=cursum
		maxj=i+1
	
print("\nThe sum :  ",end="")
print(maxsum)
print("The i :  ",end="")
print(maxi)
print("The j :  ",end="")
print(maxj)
print("The sub-Array is : ",end="")
print(a[maxi:maxj])


"""
cs1192@splc30:~/DAA LAB/emprical Analysis$ python3 maxsum_n.py 
Maximal - Sum sub-array - Effiecient Algorithm 

Enter the array : -2 -4 3 -1 5 6 -7 -2 4 3 2

The sum :  13
The i :  2
The j :  6
The sub-Array is : [3, -1, 5, 6]
cs1192@splc30:~/DAA LAB/emprical Analysis$ python3 maxsum_n.py 
Maximal - Sum sub-array - Effiecient Algorithm 

Enter the array : -1 -2 -3

The sum :  0
The i :  3
The j :  4
The sub-Array is : []

"""
