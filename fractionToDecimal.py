def fractionToDecimal(A, B):
	if A == 0:
		return 0
	if B == 0: 
		if A > 0:
			return float("inf") 
		if A < 0:
			return float("-inf") 

	x = float(A)/float(B)
	xtr =  str(x)
	xtr = str(int("".join(xtr.split("."))))
	
	if len(xtr) == 12:
		k = str(x).split(".")
		rep = k[1]

		for char in rep:
			print char
		
	else:
		return str(x)

print fractionToDecimal(22,7)