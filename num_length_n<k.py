# A =  [0, 1, 2, 5]  
# B =  2  
# C =  21

A = [0, 1, 5]
B = 1
C = 2

# A = [0, 1, 3, 5, 9]
# B = 3
# C = 545

from itertools import permutations

perm = list(permutations(A,B))
count = 0

for i in A:
	perm.append([i]*len(perm[0]))

print perm

for i in perm:
	list1 = list(i)
	print list1
	for j in xrange(0,len(list1)):
		list1[j] = str(list1[j])
	num = "".join(list1)
	print num
	if (int(num) < C) and (len(num)==B):
		count+=1

print count

# def solve(self, A, B, C):
# 	if A==[]:
# 		return 0
# 	n=len(A)
# 	C=str(C)
# 	if B > len(C):
# 		return 0
# 	if B<len(C):
# 		if B==1:
# 			return n
# 		elif A[0]==0:
# 			return (n-1)(n**(B-1))
# 	else:
# 		return n**B
# 	res=0
# 	x1=1
# 	for i in range(B):
# 		if x1==0:
# 			break
# 	r=1
# 	s=0
# 	x1=0
	
# 	for a in A:
# 		if a < int(C[i]):
# 			s=s+1
# 		elif a==int(C[i]):
# 			x1=1
# 		else:
# 			break

# 	if A[0]==0 and i==0:
# 		r=s-1
# 	else:
# 		r=s
# 	for j in range(B-1-i):
# 		r=rn
# 		res=res+r

# 	return res