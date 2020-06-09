S = "ABEC"

vowel = ['a','e','i','o','u','A','E','I','O','U']
subarray = []

# for i,elem in enumerate(S):
# 	if elem in vowel:
# 		for j in xrange(0,len(S)):
# 			if S[i:j+1] is not "":	
# 				subarray.append(S[i:j+1])

# print subarray

count = 0
for i,elem in enumerate(S):
	if elem in vowel:
		count = count + len(S) - i

print count