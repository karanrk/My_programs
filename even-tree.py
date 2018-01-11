class node(object):
    """docstring for node"""
    def __init__(self):
        #super(node, self).__init__()
        self.parent = None
        self.size=1
    
    def addparent(self,p):
        self.parent=p
        while p is not None:
            p.size+=1
            p=p.parent
            


if __name__ == '__main__':

    n,m=map(int,raw_input().split())

    nodes = [node() for _ in xrange(n)]

    for _ in xrange(m):
        child,parent=map(int,raw_input().split())
        nodes[child-1].addparent(nodes[parent-1])
    
    
    count=0
    for n in nodes:
        if n.size % 2 == 0 and n.parent != None:
            count+=1

    print count