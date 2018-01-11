#reversing a linked list

class node(object):
 	"""docstring for node"""
 	def __init__(self, val):
 		super(node, self).__init__()
 		self.val = val
 		self.next= None
 		self.head=None



def lprint(nod):
		nod.head=nod
		print 'Now head is',nod.val
		while(nod.next!=None):
			print nod.val,"-->",
			nod=nod.next
		print nod.val
	

	# if(n.next==None):
	# 	print 'n',n.val
	# 	# print 'next',n.next.val
	# 	while(n!=None):
	# 		n.next=n
# Inefficient using memory (dictionary)
def find_loop(node):
	d={}
	while (node.next!=None):
		if node not in d:
			d[node]=node
		else:
			print "loop found at node",d[node].val
			return 1
		node=node.next
	return 0

# efficient solution using "Hare and Tortoise algorithm"

def remove_loop(node):
	
	#print "trying to remove loop"
	
	fast_p=node
	slow_p=node
	sp=slow_p
	while fast_p and slow_p and fast_p.next:
		if fast_p.next.next==slow_p:
			#print "breaking"
			break
		# if fast_p==slow_p:
		# 	print "here"
		# 	break

		fast_p=node.next.next
		slow_p=node.next
		
	fast_p.next.next=None
	#print fast_p.next.val
	
	#lprint(node)

	return 1

def find_loop_efficient(node):
	hare,tort=node.head,node.head
	
	while(hare and tort and hare.next):
		hare=hare.next.next
		tort=tort.next

		if (hare==tort or hare.next==tort):
			print "Loop found at node",hare.val
			remove_loop(hare)
			return 1
			
	#print "No loop found"
	return 0



l=node(10)
l.head=l
# print "Current head of the list is",l.val
l.next=node(20)
l.next.next=node(30)
l.next.next.next=node(40)
l.next.next.next.next=l.next.next

#find_loop_efficient(l)
if(find_loop_efficient(l)==0):
	print "No loop found"

#check to see if the loop exists
lprint(l)

