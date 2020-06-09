class Node: 
    def __init__(self): 
        self.data = 0
        self.next = None

def add_nums(head1, head2):
    count1 = head1
    count2 = head2

    list1 = []
    list2 = []
    i = 1
    num1 = 0
    while count1!=None:
        list1.append(count1.data)
        num1 += i*count1.data
        count1 = count1.next
        i *= 10

    print list1, num1
    
    j = 1
    num2 = 0
    while count2!=None:
        list2.append(count2.data)
        num2 += j*count2.data
        count2 = count2.next
        j *= 10
    print list2, num2

    add = num1+num2

    print add
    
    head3 = None
    
    add = int(str(add)[::-1])
    while add:
        k = add%10
        print k
        newNode = Node()
        newNode.data = k
        newNode.next = head3
        head3 = newNode
        add = add//10

    printlist(head3)



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

add = add_nums(head1,head2)
# print add

# printlist(head2)

