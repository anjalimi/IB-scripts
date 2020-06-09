class Node: 
	def __init__(self): 
		self.data = 0
		self.next = None




def remove_dup(A):
	head = A
	temp = A
	A = A.next

	while A!=None:
		if temp.data != A.data:
			temp.next = A
			temp = A
		A = A.next
		temp.next = A

	printlist(head)


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
newNode.data = 1
head1.next = newNode 
newNode = Node() 
newNode.data = 2
head1.next.next = newNode
newNode = Node() 
newNode.data = 3
head1.next.next.next = newNode 
newNode = Node() 
newNode.data = 3
head1.next.next.next.next = newNode
head1.next.next.next.next.next = None

printlist(head1)
remove_dup(head1)



