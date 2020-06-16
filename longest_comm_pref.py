# A = ["abcdefgh", "aefghijk", "abcefgh"]

A = ["abab", "ab", "abcd"]

A = sorted(A)

a=A[0]
b=A[len(A)-1]
i=0
j=0
ans=""

while(i<len(a) and j<len(b)):
	if(a[i]==b[i]):
		ans+=a[i]
		i+=1
		j+=1
	else:
		break
print ans