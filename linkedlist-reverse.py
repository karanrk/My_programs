#reversing a linked list

class node(object):
 	"""docstring for node"""
 	def __init__(self, val):
 		super(node, self).__init__()
 		self.val = val
 		self.next= None
 		self.head=None

def preverse(curr):
	prev=None
	while(curr!=None):
		nextNode=curr.next
		curr.next=prev
		prev=curr
		curr=nextNode
	return prev

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

l=node(10)
l.head=l
# print "Current head of the list is",l.val
l.next=node(20)
l.next.next=node(30)
l.next.next.next=node(40)

lprint(l)
# print l.next.next.val
print "Calling reverse"
h=preverse(l)
lprint(h)