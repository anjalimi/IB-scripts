A = 24

if A == 1 or A == 2 or A == 3:
	print A

for x in range(0,A/2):
	if x*x == A:
		print x
		break
	elif x*x > A:
		print x-1
		break
	else:
		continue