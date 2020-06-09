A = [[1,2],[3,5],[6,7],[8,10],[12,16]]
B = [4,9]

# A = [[1,3],[6,9]]
# B = [2,5]

index_gr = [float('inf'),float('inf')]

flag = 0
for i,elem in enumerate(A):
	if elem[0] > B[0]:
		print("Element in first if",elem)
		index_gr[0] = i-1
		if B[1] > A[i-1][1]:
			index_gr[1] = i-1
		else:
			for j in xrange(i-1, len(A)):
				if A[j][1] > B[1]:
					print("Element in second if",A[j])
					index_gr[1] = j
					flag = 1
					break
	if flag == 1:
		break



	# if elem[1] > B[1]:
	# 	print("Element in second if",elem)
	# 	index_gr[1] = i+1
	# 	break

print index_gr
sublist = A[index_gr[0]:index_gr[1]+1]
print sublist

# new_elem = [min(sublist[0][0] , B[0]), max(sublist[-1][-1], B[1])]
# print new_elem

# new_list = A[0:index_gr[0]]+[new_elem]+A[index_gr[1]:]
# print new_list