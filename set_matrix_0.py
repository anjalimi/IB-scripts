A=    [   [1, 0, 1],
        [1, 1, 1],
        [1, 0, 1]   ]

col = []
row = []
for i,elem in enumerate(A):
	for j,item in enumerate(elem):
		if item == 0:
			row.append(i)
			col.append(j)

print row, col

for i, elem in enumerate(A):
	if i in row:
		A[i] = [0]*len(A[i])
	if i not in row:
		for item in col:
			A[i][item] = 0

print A



# 	if 0 in elem:
# 		elem = [0]*len(A[i])
# 		col.append(A[i].index(0))
# 		A[i] = elem
		
		
# print A, col
	
# for i, elem in enumerate(A):
# 	for item in col:
# 		A[i][item] = 0
		
# print A



