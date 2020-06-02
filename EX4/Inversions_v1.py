def inversion_count(a):
	count=0
	for i in range(len(a)-1):
		for j in range(i,len(a)):
			if(a[i]>a[j]):
				count+=1 

	return count

print("Enter the array elements : ",end="")
a=[int(x) for x in input().split()]
print()
print(a,end=" ")
print(" :",end="")
print(inversion_count(a))

"""
venky@venky-Inspiron-5570:~/DAA/EX4$ python3 Inversions_v1.py 
Enter the array elements : 1 2 3 4 5

[1, 2, 3, 4, 5]  :0

venky@venky-Inspiron-5570:~/DAA/EX4$ python3 Inversions_v1.py 
Enter the array elements : 5 4 3 2 1

[5, 4, 3, 2, 1]  :10

venky@venky-Inspiron-5570:~/DAA/EX4$ python3 Inversions_v1.py 
Enter the array elements : 3 1 2 5 4

[3, 1, 2, 5, 4]  :3

"""