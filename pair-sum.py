#Given a sorted list find if there exits a pair of numbers that add up to a given sum
#if list is not sorted, then sort it - so algorithm then will be bounded by your sorting algorithm 

#Naive approach Quadratic
#improved - n logn (sort and binary search)
#better - linear -Assumes list is sorted
#best - linear - list can be unsorted  

A=[1,-1,2,3,4,10,3,9]
#time complexity --> O(n2)
def find_sum_naive(A,s):
	for i in range(0,len(A)):
		for j in reversed(xrange(len(A))):
			#print A[i],A[j]
			if A[i]+A[j]==s:
				#print "Sum possible"
				return 1

	#print "Sum not possible"
	return 0
#time complexity --> O(nlogn)

def binary_search(A,key):
	#base case must be very precise for recursion
	if len(A)==0:
		return 0

	if len(A)==1 and A[0]==key:
		return 1

	mid=(len(A))//2
	#print "mid",mid,A

	if (A[mid]==key):
		#print"must return"
		return mid
	elif(key<A[mid]):
		#print mid
		return binary_search(A[:mid],key)
	else:
		return binary_search(A[mid+1:],key)



def find_sum_improved(A,s):
	if len(A)==0:
		return 0
	if len(A)==1 and A[0]!=s:
		return 0
	for i in range(len(A)):
		if A[i]<=s:
			k=s-A[i]
			print "searching",k,"for matching",A[i]
			print A[i+1:]
			if(binary_search(A[i+1:],k)):
				return 1
			else:
				continue

	return 0


def find_sum_best(A,s):
	i=0
	j=len(A)-1
	#print "i",i,"j",j,len(A)

	while(i<=len(A) and j>=0):
		#check if both pointers meet, if yes meaning not found
		if i==j:
			return 0
		print A[i],A[j]
		if((A[i]+A[j])==s):
			#print "mst return"
			return 1
		elif((A[i]+A[j])<s):
			i+=1
		else:
			j-=1
	print "print"		
	return 0

# list can un sorted, big idea - use hashing, hash the difference value in a dictionary and compary with element in the list
# linear running time and space is also linear (worst case when all elements are stored in dictionary)
def find_sum_efficient(A,s):
	d={}
	for i in range(len(A)):
		if A[i] in dict.itervalues(d):
				print A[i],d
				return 1
		else:
			d[A[i]]=s-A[i]
			
			

	return 0



#driver program

# if (find_sum_naive(A,8)):
# 	print "Sum possible"
# else:
# 	print "Not possible"

# if(find_sum_improved(A,8)):
# 	print "Sum possible"
# else:
# 	print "Not possible"

# if(find_sum_best(A,8)):
# 	print "Sum possible"
# else:
# 	print "Not possible"

if (find_sum_efficient(A,8)):
	print "Found"
else:
	print "not found"
