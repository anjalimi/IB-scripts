
def letter_combinations(A):
	letter_dict = {'0':'0', '1':'1', '2':['a', 'b', 'c'], '3':['d', 'e', 'f'], '4':['g', 'h', 'i'],
    	'5':['j','k','l'], '6':['m','n','o'], '7':['p','q','r','s'], '8':['t','u','v'], 
    	'9':['w','x','y','z']}

	if len(A)==1:
		return letter_dict[A[0]]

	list1 = letter_combinations(A[1:])
	res = []
	for char in letter_dict[A[0]]:
		for x in list1:
			print char,x
			s = char + x
			res.append(s)
	return sorted(res)



A = "434"

print letter_combinations(A)


