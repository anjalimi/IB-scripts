# Two ptr problem 

A = [1,2,3,-4,5,4,6]


for i in xrange(0,len(A)):
	for j in xrange(len(A)-1,i,-1):
		if i!=j and A[i]+A[j]==0:
			print "Solution: ",A[i],A[j]
			break
		if A[i]+A[j] < 0:
			break 