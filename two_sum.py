A = [ 4, 7, -4, 2, 2, 2, 3, -5, -3, 9, -4, 9, -7, 7, -1, 9, 9, 4, 1, -4, -2, 3, -3, -5, 4, -7, 7, 9, -4, 4, -8 ]
target = -3

dict1 ={}
result = []

for i,elem in enumerate(A):
	
	if elem in dict1:
		dict1[elem].append(i)
	else:
		dict1.update({elem:[i+1]})

	if target - elem in dict1:
		print target-elem, elem
		result.append([dict1[target-elem][0],i+1])

print result

print result[0]