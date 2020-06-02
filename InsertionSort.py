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

list1 = [1,3,5,7,9]
print(list1)
list1=or_ins_rec(0,list1)
print(list1)
list1=or_ins_rec(11,list1)
print(list1)
list1=or_ins_rec(4,list1)
print(list1)

"""
venky@venky-Inspiron-5570:~/DAA/EX2$ python3 InsertionSort.py 
[1, 3, 5, 7, 9]
[0, 1, 3, 5, 7, 9]
[0, 1, 3, 5, 7, 9, 11]
[0, 1, 3, 4, 5, 7, 9, 11]

"""
