#Merge Sort idea - is to divide the array until 1 element is left(base case for recursion)
#and merge until you sort the whole list - Divide and conquer algorithm (not in place as it uses extra memory for dividing the given list into two)

A=[7,3,2,10,1,2] #example list

def merge(A,L,R):
	print "merging",L,R
	
	k,i,j=0,0,0 
	while i<len(L) and j<len(R):
			if L[i]<R[j]:
				A[k]=L[i]
				i+=1
			else:
				A[k]=R[j]
				j+=1

			k+=1

			
	d=0
	e=0
	print L,R,"L and R"
	while i<len(L):
		A[k]=L[i]
		i+=1
		k+=1
	while j<len(R):
		A[k]=R[j]
		j+=1
		k+=1
				
	

	#print A
	return A



def merge_sort(A):
	
	k=len(A)
	
	if k<2:
		return 

	mid=k//2
	print mid
	L=[] * mid
	a=k-mid
	R=[] * a 
	for i in range(len(A)):
		
		if i<mid:
			#print A[:i]
			L.append(A[i])
		else:
			#print A[i+1:]
			R.append(A[i])

	print L,R
	merge_sort(L)
	merge_sort(R)
	merge(A,L,R)

merge_sort(A)
print A
