
A = "Hellel"
B = "ell"

if A is "" or B is "":
	print -1

if B not in A:
	print(-1)
else:
	print("element present")
	print(A.index(B))