#Naive Approach

A="abcb"

def first_recur(A):
	for i in xrange(len(A)):
		if A[i] in [k for k in A[i+1:]]:
			#print i
			return A[i]
	
	return None


#print (first_recur(A))
#print A[1:]

#Better Approach

def fRecur(A):
	d={}
	for i in A:

		if (i in d):
			return i
		else:
			d[i]=i
	return None

print (fRecur(A))