A = [4, 5, 3, 10, 8]

stack = []
B = []
for i,elem in enumerate(A):

	while stack!=[] and stack[-1]>=elem:
		stack.pop()

	if stack == []:
		B.append(-1)
		stack.append(elem)
		print "first"
		print B, stack
	else:
		B.append(stack[-1])
		stack.append(elem)

print B
