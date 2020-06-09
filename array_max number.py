# A = [3, 30, 34, 5, 9]
# A = [7, 20, 5]

A = [ 8, 89 ]

def comparator(a,b):
	if int(str(a)[:1]) > int(str(b)[:1]):
		return 1
	if int(str(a)[:1]) == int(str(b)[:1]):
		if a
	return -1

Asorted = sorted(A,cmp = comparator)[::-1]
print Asorted

num = ""
for elem in Asorted:
	num += str(elem)

print num

# for i in xrange(0,len(A)):
# 	for j in xrange(i+1,len(A)):
# 		if int(str(A[j])[:1]) > int(str(A[i])[:1]):
# 			B.append(A[j])
# print B

# # B = {}

# # for i,elem in enumerate(A): 
# # 	elem1 = int(str(elem)[:1])
# # 	elem2 = str(elem)[1:]
# # 	B.((elem1,elem2))

# # print B



 