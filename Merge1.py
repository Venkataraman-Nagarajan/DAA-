"""
def ordered_insert(u,List):
	for i in range(len(List)):
		if(u<List[i]):
			List.append(List[0])
			for j in range(len(List)-1,i,-1):
				List[j]=List[j-1]
			List[i]=u
			break
	else:
		List.append(u)
	return List
"""


def or_ins_rec(u,List):
	n=len(List)
	if(n==0):
		List.append(u)
		return List
	elif(u>=List[n-1] ):
		List.append(u)
		return List
	m=List[n-1:]
	lvl = or_ins_rec(u,List[:n-1]) + m
	return lvl

def ordered_merge(a,b):
	for i in a:
		b=or_ins_rec(i,b)
	return b

"""
def merge(a,b):
	c=[]
	i=0
	j=0
	while(i < len(a) and j < len(b)):
		if(a[i]<b[j]):
			c.append(a[i])
			i+=1
		else:
			c.append(b[j])
			j+=1;
	while(i<len(a)):
		c.append(a[i])
		i+=1
	while(j<len(b)):
		c.append(b[j])
		j+=1
	return c
"""

def Merge_rec(a,b):
	if(len(a)==0):
		return b
	if(len(b)==0):
		return a
	if(a[0]<b[0]):
		return a[:1]+Merge_rec(a[1:],b)
	return b[:1]+Merge_rec(a,b[1:])

def mergeSort(a):
	if(len(a)<2):
		return a
	m=len(a)//2
	return Merge_rec(mergeSort(a[:m]),mergeSort(a[m:]))

a=[2,3,6,9]
b=[0,1,7,9,12,15]
c=[1,4,2,5,3,7,4,8,6,9,7,0]
print("a : ",end="")
print(a)
print("b : ",end="")
print(b)
print("c : ",end="")
print(c)

print("\n\nOrdered-Merge(a,b)  : ",end="")
print(ordered_merge(a,b))

print("\nMergeSort of c      : ",end="")
print(mergeSort(c))
	
"""
venky@venky-Inspiron-5570:~/DAA/EX2$ python3 Merge1.py 
a : [2, 3, 6, 9]
b : [0, 1, 7, 9, 12, 15]
c : [1, 4, 2, 5, 3, 7, 4, 8, 6, 9, 7, 0]


Ordered-Merge(a,b)  : [0, 1, 2, 3, 6, 7, 9, 9, 12, 15]

MergeSort of c      : [0, 1, 2, 3, 4, 4, 5, 6, 7, 7, 8, 9]
"""	
	
