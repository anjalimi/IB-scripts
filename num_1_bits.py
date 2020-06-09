A = 4294967296

Abin = str(bin(A)[2:])

print Abin

count = 0
for i in xrange(0,32):
	if Abin[i] == "1":
		count+=1
	if i==len(Abin)-1:
		break

print count