m = 6
n = 9

def factors(num):
	factors = [1]
	for i in range(2,num/2+1):
		if num%i == 0:
			factors.append(i)
	factors.append(num)
	return factors

list1 = factors(m)


for i in sorted(list1)[::-1]:
	if n%i == 0:
		GCF = i
		break

print GCF


