def power_rec(x,n):
	if(n == 0):
		return 1
	else:
		return x * power_rec(x,n-1)


def power_itr(x,n):
	result = 1
	for i in range(n):
		result = result*x
	return result

def fast_power_rec(x,n):
	if(n==0):
		return 1
	elif(n%2 !=0):
		return x * fast_power_rec(x,n-1)
	else:
		return fast_power_rec(x,n//2) * fast_power_rec(x,n//2)

def fast_power_itr(x,n):
	result = 1
	while(n>0):
		if(n%2 == 1):
			result *= x
		n//=2
		x*=x
	return result

x,n = map(int , input("Enter Base & Exponent : ").split())
print("\nRecursive Power         : ",power_rec(x,n))
print("Iterative Power is      : ",power_itr(x,n))
print("Recursive Fast Power is : ",fast_power_rec(x,n))
print("Iterative Fast Power is : ",fast_power_itr(x,n))
	

"""
venky@venky-Inspiron-5570:~/DAA/EX2$ python3 Exponents.py 
Enter Base & Exponent : 3 5

Recursive Power         :  243
Iterative Power is      :  243
Recursive Fast Power is :  243
Iterative Fast Power is :  243
venky@venky-Inspiron-5570:~/DAA/EX2$ python3 Exponents.py 
Enter Base & Exponent : 2 6

Recursive Power         :  64
Iterative Power is      :  64
Recursive Fast Power is :  64
Iterative Fast Power is :  64

"""	
