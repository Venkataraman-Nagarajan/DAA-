"""
Q 2 n 3
"""

def partion(nut,bolt):
	pivot = len(nut)-1
	j = len(bolt)-1
	i=0
	val = nut[pivot]
	while(i<j):
		while(bolt[i]<val and i<=len(bolt)):
			i+=1
		while(bolt[j]>val and j>=-1):
			j-=1
		if(i<j):
			bolt[i],bolt[j] = bolt[j],bolt[i]
	
	pivot = i
	j = len(nut)-1
	i=0
	val = bolt[pivot]
	while(i<j):
		while(nut[i]<val and i<=len(nut)):
			i+=1
		while(nut[j]>val and j>=-1):
			j-=1
		if(i<j):
			nut[i],nut[j] = nut[j],nut[i]
	
	return nut,bolt,j

def QuickSort(nut,bolt):
	if(len(nut)<=1 or len(bolt)==1):
		return nut,bolt
	
	nut,bolt,pivot = partion(nut,bolt)
	nut_left_sorted,bolt_left_sorted 	= QuickSort(nut[:pivot],bolt[:pivot])
	nut_right_sorted,bolt_right_sorted 	= QuickSort(nut[pivot+1:],bolt[pivot+1:])
	return nut_left_sorted + nut[pivot:pivot+1] + nut_right_sorted , bolt_left_sorted + bolt[pivot:pivot+1] + bolt_right_sorted


print("\t\tBOLT n NUT PROBLEM\n")
print("NUT  : ",end="")
nut  = [int(_) for _ in input().split()]
print("BOLT : ",end="")
bolt = [int(_) for _ in input().split()]

nut,bolt = QuickSort(nut,bolt)

ans = []
i,j=0,0
while(i<len(nut) and j<len(bolt)):
	ans.append((nut[i],bolt[j]))
	i+=1
	j+=1

print("The nut & bolt pairs are : ",end="")
print(ans)

"""
venky@venky-Inspiron-5570:~/DAA/EX5$ python3 nuts_n_bolts_quicksort.py
		BOLT n NUT PROBLEM

NUT  : 2 3 4 5 6 1    
BOLT : 6 4 3 1 5 2
The nut & bolt pairs are : [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)]

"""