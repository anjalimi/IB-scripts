A = [-2,-1]

maxSum = A[0]
partialSum = 0

for i,elem in enumerate(A):
	if partialSum+elem < 0: #So that we never check the elements that make partial sum <0
		partialSum = 0
		continue

	partialSum += elem
	
	if (partialSum > maxSum):
		maxSum = partialSum
	
	print("Elem:", elem, " Maxsum: ", maxSum)

	if (maxSum == A[0]):
		print max(A)

print maxSum
