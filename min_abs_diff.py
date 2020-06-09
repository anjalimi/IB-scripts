# A = [ 1, 4, 5, 8, 10 ]
# B = [ 6, 9, 15 ]
# C = [ 2, 3, 6, 6 ]

# A = [-1, -2, -3]
# B = [-4, -5, -6]
# C = [1, 2, 3]

A = [1, 4, 10]
B = [2, 15, 20]
C = [10, 12]

i,j,k = 0,0,0
ans = max(A[0],B[0],C[0])-min(A[0],B[0],C[0])

while i < len(A) or j < len(B) or k < len(C):
	ans=min(ans,max(A[i],B[j],C[k])-min(A[i],B[j],C[k]))
    
	if A[i]==min(A[i],B[j],C[k]) and i<len(A)-1:
		i+=1
	elif B[j]==min(A[i],B[j],C[k]) and j<len(B)-1:
		j+=1
	elif C[k]==min(A[i],B[j],C[k]) and k<len(C)-1:
		k+=1
	else:  
		break

print ans




