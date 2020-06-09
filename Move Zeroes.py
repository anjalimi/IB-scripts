A = [1,1,1,3,12]

for elem in A:
	if elem ==  0:
		A.remove(elem)
		A.append(0)
print A