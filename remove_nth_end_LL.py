class Node: 
    def __init__(self): 
        self.data = 0
        self.next = None


def remove_n(A,n):
	head1 = A
	size = 0
	while A:
		size += 1
		A = A.next
	
	if n > size:
		return head1

	remove_node = size - n
	node = 0

	A = head1
	while A:
		if node == remove_node-1:
			print remove_node-1, node
			A.next = A.next.next
			A = A.next
		else:
			A = A.next
		node += 1

	return head1


def printlist(list1):
    count = list1
    list_out = []
    while count!= None:
        list_out.append(count.data) 
        count = count.next
    print list_out


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
# head1.next.next.next.next = None
newNode = Node() 
newNode.data = 5
head1.next.next.next.next = newNode
head1.next.next.next.next.next = None

printlist(head1)
head3 = remove_n(head1, 1)
printlist(head3)