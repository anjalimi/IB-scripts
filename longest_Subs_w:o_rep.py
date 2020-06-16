def substring_norepeat(A):
	str1 = ""
	res =[]
	i = 0
	dict1 = {}
	while i <len(A):
		if A[i] not in str1:
			# print A[i], str1, "<---"
			str1+=A[i]
			dict1.update({A[i]:i})
			i+=1
			if i==len(A):
				# print str1
				res.append(str1)
		else:
			# print A[i], dict1
			j = dict1[A[i]]
			res.append(str1)
			# print res
			str1  = ""
			i = j+1
		
	return max(res, key=len)


# A = "abcabcbb"
# A = "abcaz"

A = "dadbc"
# ans = adbc

A = "bbbbb"

print substring_norepeat(A)