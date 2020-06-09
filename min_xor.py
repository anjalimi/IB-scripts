A = [0, 2, 5, 7]

# A = [0, 4, 7, 9]
A = sorted(A)
minxor = A[0]^A[1]

for i in xrange(0,len(A)-1):
	xor = A[i]^A[i+1]
	print A[i], A[i+1]
	print xor
	minxor = min(minxor, xor)

print minxor