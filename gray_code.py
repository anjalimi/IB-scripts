def helper(A):
	res = []
	if A == 0:
		res.append('0')
		return res
	if A == 1:
		res.append('0')
		res.append('1')
		return res

	x = helper(A-1)
	for i,elem in enumerate(x):
		if i%2==0:
			str1 = elem+'0'
			str2 = elem+'1'
		else:
			str1 = elem+'1'
			str2 = elem+'0'
		res += [str1,str2]
	return res

def grayCode(A):

	resultBin = helper(A)
	print resultBin
	
	B = []
	for elem in resultBin:
		elem = int(elem,base=2)
		B.append(elem)

	return B

n = 5
print grayCode(n)