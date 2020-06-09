def reverseList(self, A):
    if not A or not A.next:
        return A
    p = self.reverseList(A.next)
    A.next.next = A
    A.next = None
    return p