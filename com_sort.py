#combined sort insertion and quick sort
#The Big idea Use Insertion sort where range of numbers is less and use quick_sort if otherwise

A=[8,12,12,7,5,11,4,10,3]

def insertion_sort(A):
	for j in range(1,len(A)):
		i=j-1
		key=A[j]
		while i>=0 and key < A[i]:
			A[i+1]=A[i]
			i-=1
		A[i+1]=key

	return A

def partion(A):
	pivot=A[-1]
	A=A[:-1]
	low=[x for x in A if x<=pivot]
	high=[x for x in A if x>pivot]
	return low,pivot,high

def quick_sort(A):
	if (len(A))==0:
		return A
	low,pivot,high=partion(A)
	return quick_sort(low)+[pivot]+quick_sort(high)

# Main sorting logic	
def combined_sort(A):
	high=max(A)
	low=min(A)
	if len(A)<=1:
		return A

	#threshold value set to 9
	if(high-low<=9):
		print "Insertion Sort will be used"
		return (insertion_sort(A))
	else:
		print "Quick Sort will be used"
		return (quick_sort(A))
		 
print(combined_sort(A))
