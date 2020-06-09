class Node: 
    def __init__(self): 
        self.data = 0
        self.next = None

def list_cycle(list1):
	count = list1
	nodes = set()
	while count:
		if count in nodes:
			print "Duplicate:", count
			break
		else:
			nodes.add(count)
			count=count.next

	print "found"

def printlist(list1):
    count = list1
    list_out = []
    node_list = [count]
    i = 0
    while count!= None:
    	# print count.data
    	node_list.append(count.next)
        list_out.append(count.data) 
        count = count.next
        i+=1
        if i>10:
        	break
    
    print list_out
    print node_list


newNode = None
head1 = Node() 
head1.data = 1
newNode = Node() 
newNode.data = 2
head1.next = newNode 
newNode = Node() 
newNode.data = 3
head1.next.next = newNode
newNode = Node() 
newNode.data = 4
head1.next.next.next = newNode
head1.next.next.next.next = head1.next.next

printlist(head1)
list_cycle(head1)

