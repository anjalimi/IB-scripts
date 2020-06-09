class Node: 
    def __init__(self): 
        self.data = 0
        self.next = None


def get_middle(list1):
	if list1 == None:
		return list1
	slow = list1 
	fast = list1 
	while (fast.next != None and fast.next.next != None): 
		slow = slow.next
		fast = fast.next.next
	return slow

def reverse_secondhalf(list1):
	prev = None
	curr = list1
	next = None

	while curr != None:
		next = curr.next
		curr.next = prev
		prev = curr
		curr = next

	return prev

def reorder(list1):
	middle = get_middle(list1)
	nexttomiddle = middle.next
	reversed_list = reverse_secondhalf(middle.next)
	printlist(reversed_list)

	curr = list1
	sec = reversed_list
	while True:
		if not curr or not sec:
			break
		if curr.next == sec:
			break
		print curr.data, sec.data
		next_o = curr.next
		next_r = sec.next
		
		curr.next = sec
		sec.next = next

		curr = next_o
		sec = next_r

	printlist(list1)
	

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
reorder(head1)