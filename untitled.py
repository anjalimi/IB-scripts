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
head1.next.next.next.next = None
