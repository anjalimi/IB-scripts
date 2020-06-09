class Node: 
    def __init__(self): 
        self.data = 0
        self.next = None



def printlist(list1):
    count = list1
    list_out = []
    while count!= None:
        list_out.append(count.data) 
        count = count.next
    print list_out,"sbcd"


newNode = None
head1 = Node() 
head1.data = 2
newNode = Node() 
newNode.data = 4
head1.next = newNode 
newNode = Node() 
newNode.data = 3
head1.next.next = newNode
head1.next.next.next = None

newNode = None
head2 = Node() 
head2.data = 5
newNode = Node() 
newNode.data = 6
head2.next = newNode 
newNode = Node() 
newNode.data = 4
head2.next.next = newNode
head2.next.next.next = None

printlist(head1)
printlist(head2)

