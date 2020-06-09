def permute(A):
	res = []
	if len(A) == 1:
		return [A]

	for elem in A:
		rest = [e for e in A if e!=elem]
		list1 = permute(rest)

		for i in list1:
			i.append(elem)
		
		res = res + list1
		print res
	return sorted(res)


A = [1,2,3]
print permute(A)
