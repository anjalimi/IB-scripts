def letterCasePermutation(S):
	"""
	:type S: str
	:rtype: List[str]
	"""
	res = []
	if S.isdigit():
		res.append(S)
		return res
	if len(S)==1:
		res.append(S.lower())
		res.append(S.upper())
		return res
	x = letterCasePermutation(S[1:])
	elem = S[0]
	for item in x:
		if elem.isalpha():
			res.append(elem.lower()+item)
			res.append(elem.upper()+item)
		else:
			res.append(elem+item)

	return sorted(res)

# S = "ab"
# expected = ["ab","aB","Ab","AB"]
# S = "abc"
# expected = ["abc","abC","aBc","aBC","Abc","AbC","ABc","ABC"]
# S = "12345"
S = "a1b2"

print letterCasePermutation(S)
