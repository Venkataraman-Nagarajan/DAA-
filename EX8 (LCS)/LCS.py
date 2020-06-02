print("LCS--\nEnter 'a' string  : ",end="")
a=input()
print("Enter 'b' string  : ",end="")
b=input()

dp=[[0 for i in range(len(b)+1)] for _ in range(len(a)+1) ]

for i in range(1,len(a)+1):
	for j in range(1,len(b)+1):
		if(a[i-1]==b[j-1]):
			dp[i][j]=dp[i-1][j-1]+1
		else:
			dp[i][j]=max(dp[i-1][j],dp[i][j-1])

print("The LCS count is : ",end="")
print(dp[len(a)][len(b)])

ans=""
i,j = len(a),len(b)
while(i>0 and j>0):
	if(a[i-1]==b[j-1]):
		ans = ans + a[i-1]
		i-=1
		j-=1
	else:
		if(dp[i][j-1] > dp[i-1][j]):
			j-=1
		else:
			i-=1
print("LCS String is    : ",end="")
print(ans[::-1])

"""
cs1192@splc30:~/DAA LAB/LCS$ python3 LCS.py 
LCS--
Enter 'a' string  : abcdef 
Enter 'b' string  : abef
The LCS count is : 4
LCS String is    : abef
cs1192@splc30:~/DAA LAB/LCS$ python3 LCS.py 
LCS--
Enter 'a' string  : aggtab
Enter 'b' string  : gxtxayb
The LCS count is : 4
LCS String is    : gtab
"""
