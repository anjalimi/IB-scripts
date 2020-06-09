class Node: 
    def __init__(self): 
        self.data = 0
        self.next = None

def sortedMerge(a, b): 
        result = None
        if a == None: 
            return b 
        if b == None: 
            return a 
        if a.data <= b.data: 
            result = a 
            result.next = sortedMerge(a.next, b) 
        else: 
            result = b 
            result.next = sortedMerge(a, b.next) 
        return result 
      
def mergeSort(h): 

    if h == None or h.next == None: 
        return h 
    middle = getMiddle(h) 
    nexttomiddle = middle.next
    middle.next = None
    left = mergeSort(h) 
    right = mergeSort(nexttomiddle)  
    sortedlist = sortedMerge(left, right) 
    return sortedlist 
       
def getMiddle(head): 
    if (head == None): 
        return head 
    slow = head 
    fast = head 
    while (fast.next != None and 
           fast.next.next != None): 
        slow = slow.next
        fast = fast.next.next
    return slow


def printlist(list1):
    count = list1
    list_out = []
    i = 0
    while count!= None:
        list_out.append(count.data) 
        count = count.next
        i+=1
        if i>10:
        	break
    
    print list_out


newNode = None
head1 = Node() 
head1.data = 1
newNode = Node() 
newNode.data = 5
head1.next = newNode 
newNode = Node() 
newNode.data = 4
head1.next.next = newNode
newNode = Node() 
newNode.data = 3
head1.next.next.next = newNode
head1.next.next.next.next = None

printlist(head1)
sortedlist = mergeSort(head1)
printlist(sortedlist)