# A = [3, 4, 1, 4, 1]

A = [1,2]


A = sorted(A)
duplicate = -1
for i in xrange(0, len(A)-1):
	if A[i+1] == A[i]:
		duplicate =  A[i]
		break

print duplicate


	


