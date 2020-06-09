# A = [1, 5, 7, 8] 
A = [1,3,5]
k = 4

for i in xrange(0,len(A)):
	for j in xrange(len(A)-1,i,-1):
		if i!=j and abs(A[i]-A[j])==k:
			print i,j
			print "Solution: ",A[i],A[j]
			break


