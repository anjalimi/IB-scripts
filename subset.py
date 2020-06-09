# Given a set of distinct integers, S, return all possible subsets.

# Note:
# Elements in a subset must be in non-descending order.
# The solution set must not contain duplicate subsets.
# Also, the subsets should be sorted in ascending ( lexicographic ) order.
# The list is not necessarily sorted.


def subsets(A):
	if A == []:
		return [[]]
	x = subsets(A[1:])
	z = [[A[0]] + y for y in x]
	return sorted(x + z)

		

A = [1,2,3]
A = sorted(A)

print subsets(A)