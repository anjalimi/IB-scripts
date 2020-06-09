A = [ 4, 6, 5, 5, 6, 6, 5, 6, 7, 5, 5, 7, 7 ]

def leftSpecialVal(i, A):
	left = []
	for item in xrange(0,i):
		if A[item] > A[i]:
			left.append(item)
	if len(left) == 0:
		return 0
	return max(left)

def rightSpecialVal(i, A):
	right = []

	for item in xrange(i+1,len(A)):
		if A[item] > A[i]:
			right.append(item)
	if len(right) == 0:
		return 0
	return min(right)

specialProdList = []
for i,elem in enumerate(A):
	left = leftSpecialVal(i,A)
	right = rightSpecialVal(i,A)
	print "Left Value:  ", left, " right value:  ", right
	specialProd = left * right
	print specialProd
	specialProdList.append(specialProd)

print max(specialProdList)


