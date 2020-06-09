A = [ 11, 8, 7, 9, 2, 10, 2 ]

# A = [1,2,3,4]
A = sorted(A)


# a1>=a2<=a3>=a4
for i,elem in enumerate(A):
	print i
	if i%2==0 and i!=(len(A)-1):
		if elem >= A[i+1]:
			pass
		else:
			A[i],A[i+1] = A[i+1],A[i]
			print "Swapped : even --> ", A
	if i%2==1 and i!=(len(A)-1):
		if elem <= A[i+1]:
			pass
		else:
			A[i],A[i+1] = A[i+1],A[i]
			print "Swapped : ODD --> ", A
			
