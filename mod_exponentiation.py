def Mod(A,B,C):
	if B == 0:
		return 1
	elif B%2 == 0:
		num = Mod(A,B/2,C)
		return num*num % C

	else:
		return ((A%C) * Mod(A, B-1, C)) % C


# 2^3 % 3
print Mod(2,3,3)
