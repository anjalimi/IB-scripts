A = [ 0, 0, -1, 0 ]

list1 = []
list2 = []
for i,elem in enumerate(A):
	if elem >= 0: 
		list2.append(elem)
		print list2
	else:
		list1.append(list2)
		print list1
		list2 = []

list1.append(list2)
print "non negative list:",list1

maxsum = 0
vector = []
for elem in list1:
	if sum(elem)>maxsum:
		vector = elem
		maxsum = sum(elem)
	elif sum(elem) == maxsum:
		print elem, vector
		if len(elem) == len(vector):
			if len(elem) == 0:
				vector = [] 
			elif elem[0] < vector[0]:
				vector = elem
		else:
			if len(elem) > len(vector):
				vector = elem


print "The max summing element is: ", vector, "maxsum : ", maxsum 