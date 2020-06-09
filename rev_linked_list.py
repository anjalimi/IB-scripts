class Node: 
	def __init__(self): 
		self.data = 0
		self.next = None



# Create one linked lists 
  
# 1st Linked list is 3.6.9.15.30 
      
# 15 is the intersection point 

def printlist(list1):
	count = list1
	list_out = []
	while count!= None:
		list_out.append(count.data) 
		count = count.next
	print list_out


newNode = None
head1 = Node() 
head1.data = 10
head2 = Node() 
head2.data = 3
newNode = Node() 
newNode.data = 6
head2.next = newNode 
newNode = Node() 
newNode.data = 9
head2.next.next = newNode 
newNode = Node() 
newNode.data = 15
head1.next = newNode 
head2.next.next.next = newNode 
newNode = Node() 
newNode.data = 30
head1.next.next = newNode 
head1.next.next.next = None

printlist(head1)
printlist(head2)

