def MaxCrossingSum(a,l,r,m):
	Sum=0
	left_sum=0

	for i in range(m,l-1,-1):
		Sum+=a[i]
		if(left_sum < Sum):
			left_sum=Sum

	Sum=0
	right_sum=0

	for i in range(m+1,r+1):
		Sum+=a[i]
		if(right_sum < Sum):
			right_sum=Sum

	return left_sum+right_sum

def MaxSumSide(a,l,r):
	if(l==r):
		return a[l]

	m=(l+r)//2	

	return max(MaxSumSide(a,l,m),MaxSumSide(a,m+1,r),MaxCrossingSum(a,l,r,m))

print("Enter the elements of the array : ",end="")
a=[int(x) for x in input().split()]
print("Maximum sum is : ",end="")
print(MaxSumSide(a,0,len(a)-1))


"""
venky@venky-Inspiron-5570:~/DAA/EX3$ python3 maxsum_nlogn.py 
Enter the elements of the array : -1 -2 
Maximum sum is : 0
venky@venky-Inspiron-5570:~/DAA/EX3$ python3 maxsum_nlogn.py 
Enter the elements of the array : 2 1 3 4 -9 -4 3 1
Maximum sum is : 10
venky@venky-Inspiron-5570:~/DAA/EX3$ python3 maxsum_nlogn.py 
Enter the elements of the array : 2 1 3 4 -3 -4 9 1
Maximum sum is : 13

"""