# generate all subarrays of A.
# take the maximum element from each subarray of A and insert it into a new array G.
# replace every element of G with the product of their divisors mod 1e9 + 7.
# sort G in descending order
# perform Q queries
# In each query, you are given an integer K, where you have to find the Kth element in G.

# A = [ 39, 99, 70, 24, 49, 13, 86, 43, 88, 74, 45, 92, 72, 71, 90, 32, 19, 76, 84, 46, 63, 15, 87, 1, 39, 58, 17, 65, 99, 43, 83, 29, 64, 67, 100, 14, 17, 100, 81, 26, 45, 40, 95, 94, 86, 2, 89, 57, 52, 91, 45 ]
# 

A = [1, 2, 4]
B = [1, 2, 3, 4, 5, 6]
def countFactors(n) : 
	count = 0
	i = 1
	while i * i <= n : 
		if (n % i == 0) : 
			if (n / i == i) : 
				count = count + 1
			else : 
				count = count + 2
		i = i + 1
	return count


def sub_lists(list1): 
	sublist = [] 
	for i in range(len(list1) + 1): 
		for j in range(i + 1, len(list1) + 1): 
			sub = list1[i:j] 
			if len(sub)!= 0:
				sublist.append(sub)

	return sublist

sublist = sub_lists(A)
G = []
for elem in sublist:
	newElem = max(elem)
	prod = 1
	numFactors = countFactors(newElem)
	print numFactors, newElem
	D = newElem**(numFactors/2)
	if numFactors%2 == 1:
		D = D*(newElem**0.5)
	prod = int(D%(1e9 + 7))
	# for i in xrange(1,newElem+1):
	# 	if newElem%i == 0:
	# 		prod*=i
	print newElem, "-->", prod
	G.append(prod)

G = sorted(G, reverse = 1)
# print G

X = []
for i in B: 
	X.append(G[i-1])

print X