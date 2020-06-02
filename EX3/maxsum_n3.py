print("Maximal - Sum sub-array - Brute Approach ")
print("\nEnter the array : ",end="")
a=[int(_) for _ in input().split()]

n=len(a)
maxi = -1
maxj = -1
maxsum=0;
for i in range(0,n):
	for j in range(i,n):
		Sum=0
		Sum=sum(a[i:j+1])
		if(maxsum < Sum):
			maxsum=Sum
			maxi=i
			maxj=j	
print("\nThe sum :  ",end="")
print(maxsum)
print("The i :  ",end="")
print(maxi)
print("The j :  ",end="")
print(maxj+1)
print("The sub-Array is : ",end="")
print(a[maxi:maxj+1])

"""
cs1192@splc30:~/DAA LAB/emprical Analysis$ python3 maxsum_n3.py 
Maximal - Sum sub-array - Brute Approach 

Enter the array : -2 -4 3 -1 5 6 -7 -2 4 3 2

The sum :  13
The i :  2
The j :  6
The sub-Array is : [3, -1, 5, 6]
"""
