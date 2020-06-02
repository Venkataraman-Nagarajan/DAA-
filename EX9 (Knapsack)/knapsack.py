import math

print("Knapsack problem \n")
print("Enter knapsack weight : ",end="")
W = int(input())
print()
print("Enter n weights :  ",end="")
weight = [int(_) for _ in input().split()]
print("Enter n prices  :  ",end="")
price =  [int(_) for _ in input().split()]

dp = [[ -1 for i in range(W+1)] for j in range(len(weight)) ]



def solve(w,n):
	if(dp[n][w]!=-1):
		return dp[n][w]
	if(w<0 or n<0):
		return -math.inf 
	if(w==0 or n==0):
		dp[n][w]=0
		return dp[n][w]
	dp[n][w]=max(solve(w,n-1),solve(w-weight[n],n-1)+price[n])
	return dp[n][w]
	
print("\nThe max cost that can be incorporated is : ",end="")
print(solve(W,len(weight)-1))

"""
cs1192@splc30:~/DAA LAB/01-Knapsack$ python3 knapsack.py 
Knapsack problem 

Enter knapsack weight : 50

Enter n weights :  10 20 30
Enter n prices  :  60 100 120

The max cost that can be incorporated is : 220
"""
