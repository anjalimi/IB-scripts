A = [1,1,2,3,5,7,7,7,7,7,7,7,8]

B = 0

if B in A: 
	start = A.index(B)
else:
	return 0
print start
count = 0
for i in xrange(start,len(A)):
	if A[i] == B:
		count+=1
	else:
		break
print count