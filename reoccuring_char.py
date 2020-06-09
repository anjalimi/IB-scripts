# RETURN FIRST REOCCURING CHAR
A =[2,3,4,5,6,2,4,5,6]

dict1 = {}

for elem in A:
	if elem in dict1:
		print elem
		break
	else:
		dict1.update({elem:1})

print -1