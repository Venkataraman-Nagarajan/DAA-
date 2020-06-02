def pair(a,b):
	req = []

	for i in range(len(a)):
		for j in range(len(b)):
			if(a[i]==b[j]):
				req.append((i+1,j+1))

	return req


print("\t\tBOLT n NUT PROBLEM\n")
print("NUT  : ",end="")
nut  = [int(_) for _ in input().split()]
print("BOLT : ",end="")
bolt = [int(_) for _ in input().split()]

matched_pairs = pair(nut,bolt)

print("The matched pair indices :  ",end="")
print(matched_pairs)


"""
venky@venky-Inspiron-5570:~/DAA/EX5$ python3 nuts_n_bolts_n2.py 
		BOLT n NUT PROBLEM

NUT  : 1 4 2 5 3
BOLT : 5 2 4 1 3
The matched pair indices :  [(1, 4), (2, 3), (3, 2), (4, 1), (5, 5)]

"""