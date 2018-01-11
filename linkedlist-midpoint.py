#find midpoint and swap 2 nodes in a linked list

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

def find_mid(node):
	p1,p2=node.head,node.head

	while(p1 and p2 and p2.next):
		p1=p1.next
		p2=p2.next.next

	return p1.val

#algorithm to swap two nodes
def swap_node(nod,node1,node2):
	p1,p2=nod.head,nod.head.next
	print node1.val,node2.val
	lprint(node2)
	n=node2
	
	
	if node2.next==None:
		n2=None

	n1=node1.next
	n2=node2.next

	while(p1 and p2.next):
		
		if node1==nod.head:
			n3=None

		if p2==node1:
			n3=p1
			print "n3",p1.val
		if p2==node2:
			n4=p1
			print "n4",n4.val
		if p2.next.next==None:
			n4=p1
			break
		p1,p2=p1.next,p2.next

	 	
	
	
	node2=n3.next
	
	node1=n4.next
	
	
	node1.next=n2
	node2.next=n1
	
	if p2.next==None:
		node1=n
	

	print node1.val,node2.val
	lprint(node2)

		


		



n=node(1)
n.head=n
n.next=node(2)
n.next.next=node(3)
n.next.next.next=node(4)
n.next.next.next.next=node(5)

#lprint(n)
#print(find_mid(n))
print (swap_node(n,n.next.next,n.next.next.next.next))
