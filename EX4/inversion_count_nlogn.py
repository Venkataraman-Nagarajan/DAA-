def merge(a,temp,l,mid,h):
	i=l
	k=l
	j=mid+1
	inv_count=0
	while((i<=mid) and j<=h):
		if(a[i]<a[j]):
			temp[k]=a[i]
			k+=1
			i+=1	
		else:
			temp[k]=a[j]
			k+=1
			j+=1
			inv_count+=mid-i+1
	
	while(i<=mid):
		temp[k]=a[i]
		k+=1
		i+=1
	
	while(j<=h):
		temp[k]=a[j]
		k+=1
		j+=1
	
	return inv_count

def mergesort(a,temp,l,h):
	inv_count=0
	
	if(l<h): 
		mid = (l+h)//2
		
		inv_count+=mergesort(a,temp,l,mid)
		inv_count+=mergesort(a,temp,mid+1,h)
		inv_count+=merge(a,temp,l,mid,h)
		
	return inv_count

def countInv(a):
	temp = [0 for i in range(len(a))]
	return mergesort(a,temp,0,len(a)-1)

a=[int(x) for x in input().split() ]
print("The inversion count is : ",countInv(a))


"""
cs1192@splc30:~/DAA LAB/Inversion_count$ python3 inversion_count_nlogn.py 
2 1 3 4 5
The inversion count is :  1
cs1192@splc30:~/DAA LAB/Inversion_count$ python3 inversion_count_nlogn.py 
2 3 1 5 4
The inversion count is :  3
cs1192@splc30:~/DAA LAB/Inversion_count$ python3 inversion_count_nlogn.py 
1 2 3 4 5
The inversion count is :  0
"""
