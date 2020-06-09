A = [1, 2, 2]

Adict = {}

for elem in A:
	if elem not in Adict:
		Adict.update({elem:1})
	else:
		count = Adict[elem]
		Adict.update({elem:count+1})

for elem in Adict:
	if Adict[elem]==1:
		print elem
		break
	
