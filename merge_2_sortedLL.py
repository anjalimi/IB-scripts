class Node: 
    def __init__(self): 
        self.data = 0
        self.next = None



def merge(A,B):
    dummy = Node()
    current = dummy
    current.data = -1

    while 1:
        if A == None:
            current.next = B
            break
        if B == None:
            current.next = A
            break
        # print ("ABABAB")
        # printlist(A)
        # printlist(B)
        # printlist(dummy.next)
        if A.data <= B.data:
            current.next = A
            A = A.next
        else:
            current.next = B
            B = B.next

        current = current.next


    return dummy.next


def printlist(list1):
    count = list1
    list_out = []
    while count!= None:
        list_out.append(count.data) 
        count = count.next
    print list_out


newNode = None
head1 = Node() 
head1.data = 2
newNode = Node() 
newNode.data = 2
head1.next = newNode 
newNode = Node() 
newNode.data = 3
head1.next.next = newNode
head1.next.next.next = None

# head1 = None

newNode = None
head2 = Node() 
head2.data = 1
newNode = Node() 
newNode.data = 5
head2.next = newNode 
newNode = Node() 
newNode.data = 6
head2.next.next = newNode
head2.next.next.next = None

# printlist(head1)
# printlist(head2)

head3 = merge(head1, head2)
printlist(head3)
